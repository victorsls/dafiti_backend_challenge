from django.db import models

# Create your models here.


class Shoes(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=100)
    description = models.TextField(verbose_name="Descrição")
    width = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to="product_images",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "shoes"
        verbose_name = "Sapato"
        verbose_name_plural = "Sapatos"
