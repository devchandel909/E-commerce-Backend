from django.urls import path
from .views import CartCreatAPIView

urlpatterns = [

    path(
        'cart',
        CartCreatAPIView.as_view(),
        name='cart-create'
    ),

]