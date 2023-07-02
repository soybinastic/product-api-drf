from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.product.name} - {self.comment}'
