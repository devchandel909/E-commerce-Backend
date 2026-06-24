from rest_framework.routers import DefaultRouter
from .views import ProductViewSets ,ProductImageDeleteView,ProductImageUploadView
from django.urls import path


router=DefaultRouter()
router.register('products',ProductViewSets,basename='product')

urlpatterns=  router.urls

urlpatterns= router.urls + [
    
    path(
    'products/images/<int:pk>/',
    ProductImageUploadView.as_view(),
    name='product-image-upload'
),

path(
    'images/delete/<int:pk>/',
    ProductImageDeleteView.as_view(),
    name='product-image-delete'
),
    
    
]