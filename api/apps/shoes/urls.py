from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apps.shoes.views import ShoesUploadCsvFileView, ShoesViewSet

app_name = "shoes"

router = DefaultRouter()
router.register("shoes", ShoesViewSet, basename="shoes")

urlpatterns = [
    path("shoes-csv/", ShoesUploadCsvFileView.as_view(), name="shoes_csv")
] + router.urls
