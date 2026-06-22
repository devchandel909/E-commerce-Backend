from django.urls import path

from .views import (
    WishlistView,
    WishlistDeleteView
)

urlpatterns = [

    path(
        'wishlist/',
        WishlistView.as_view(),
        name='wishlist'
    ),

    path(
        'wishlist/<int:product_id>/',
        WishlistDeleteView.as_view(),
        name='wishlist-delete'
    )
]