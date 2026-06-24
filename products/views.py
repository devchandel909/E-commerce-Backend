from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Product,ProductImage
from .serializers import ProductSerializer,ProductImageSerializer

from categories.permissions import IsAdminOrReadOnly
from rest_framework.generics import (DestroyAPIView)

class ProductViewSets(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

    # Filtering and Searching
    filter_backends = [DjangoFilterBackend, SearchFilter]

    # Filtering
    filterset_fields = ['category', 'brand']

    # Searching
    search_fields = ['name', 'description']
    
    
class ProductImageUploadView(APIView):
    
    permission_classes = [
        IsAdminOrReadOnly
    ]


    def post(self, request, pk):

        data = request.data.copy()

        data['product'] = pk #product_id

        serializer = ProductImageSerializer(
            data=data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
        
class ProductImageDeleteView(DestroyAPIView):

    queryset = ProductImage.objects.all()

    serializer_class = ProductImageSerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
# Single + Multiple Create
    def create(self, request, *args, **kwargs):
        
        
        
# ye check karega ki single data he ya muliple data he 
        many = isinstance(request.data, list)
        
        
        #get_serilizer modelviewset ka built in method he jo cuurecct viewset me jo viewset he uska object banata he taki uski sari properties use krr ske

        serializer = self.get_serializer(
            data=request.data,
            many=many
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

'''
