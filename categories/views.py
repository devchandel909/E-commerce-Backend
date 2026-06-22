
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView)

from .models import Category
from .serializers import CategorySerializer
from .permissions import  IsAdminOrReadOnly


class CategoryListCreateView(ListCreateAPIView):

    

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):

    

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]