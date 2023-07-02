from django.db import models
from product.models import Product

# Create your models here.


class Category(models.Model):

    class Meta:
        db_table = 'categories'

    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='categories', through='ProductCategory')

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'

class ProductCategory(models.Model):
    class Meta:
        db_table = 'product_categories'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)