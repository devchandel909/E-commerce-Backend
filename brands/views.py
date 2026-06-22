from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Brand
from .serializers import BrandSerializer
from categories.permissions import IsAdminOrReadOnly


class BrandListCreateView(ListCreateAPIView):

    queryset = Brand.objects.all()

    serializer_class = BrandSerializer

    permission_classes = [IsAdminOrReadOnly]


class BrandDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Brand.objects.all()

    serializer_class = BrandSerializer

    permission_classes = [IsAdminOrReadOnly]