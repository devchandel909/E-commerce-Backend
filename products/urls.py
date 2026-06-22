from rest_framework.routers import DefaultRouter
from .views import ProductViewSets ,ProductImageDeleteView,ProductImageUploadView
from django.urls import path


router=DefaultRouter()
router.register('products',ProductViewSets,basename='product')

urlpatterns=  router.urls

urlpatterns= router.urls + [
    
    path(
    'products/<int:pk>/images/',
    ProductImageUploadView.as_view(),
    name='product-image-upload'
),

path(
    'images/<int:pk>/delete/',
    ProductImageDeleteView.as_view(),
    name='product-image-delete'
),
    
    
]