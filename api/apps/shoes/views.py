import pandas as pd
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.apps.shoes.models import Shoes
from api.apps.shoes.serializers import ShoesSerializer, ShoesUploadCsvFileSerializer


class ShoesViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FileUploadParser)
    renderer_classes = (JSONRenderer,)
    serializer_class = ShoesSerializer
    queryset = Shoes.objects.all()


class ShoesUploadCsvFileView(CreateAPIView):
    parser_classes = (MultiPartParser, FileUploadParser)
    renderer_classes = (JSONRenderer,)
    serializer_class = ShoesSerializer
    serializer_class = ShoesUploadCsvFileSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data["file"]
        reader = pd.read_csv(file, sep=";", converters={"width": int})
        for _, row in reader.iterrows():
            new_shoes = Shoes(
                title=row["title"],
                description=row["description"],
                width=row["width"],
            )
            new_shoes.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
