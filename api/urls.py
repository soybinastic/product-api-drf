from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductAPI, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
urlpatterns = [
    path('' , include(router.urls))
]