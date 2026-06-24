from django.urls import path

from .views import (
    CreateOrderView,
    OrderListView,
    OrderDetailView
)

urlpatterns = [

    path(
        'order/get/',
        OrderListView.as_view(),
        name='orders'
    ),

    path(
        'order/create/',
        CreateOrderView.as_view(),
        name='create-order'
    ),

    path(
        'order/<int:pk>/',
        OrderDetailView.as_view(),
        name='order-detail'
    ),
]