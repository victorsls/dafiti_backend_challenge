from rest_framework import serializers

from api.apps.shoes.models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = "__all__"


class ShoesUploadCsvFileSerializer(serializers.Serializer):
    file = serializers.FileField()
