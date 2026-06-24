from django.urls import path

from .views import *

urlpatterns = [

    path(
        'address/',
        AddressView.as_view(),
        name='address-list-create'
    ),

    path(
        'address/update/<int:pk>/',
        AddressUpdateView.as_view(),
        name='address-update'
    ),

    path(
        'address/delete/<int:pk>/',
        AddressDeleteView.as_view(),
        name='address-delete'
    ),
]