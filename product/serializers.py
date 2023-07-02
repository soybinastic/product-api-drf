from rest_framework.serializers import ModelSerializer, SlugRelatedField, ValidationError
from .models import Product
from category.models import Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'categories']

    def validate_name(self, value):

        name = str(value).title()
        if name != value:
            raise ValidationError(f'The product name should be title casing. (ex. {name})')
        
        if Product.objects.filter(name__iexact=value).exists():
            raise ValidationError(f'{name} product is already exist!')
        
        return name
    def validate_price(self, value):

        if value < 50:
            raise ValidationError('Price must be more than 50 or equal!')
        return value
    
    