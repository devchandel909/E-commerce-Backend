from django.shortcuts import render
from .serializers import CartSerializer
from products.models import Product
from .models import Cart_item
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
class CartCreatAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        
        
        
        #request.data.get('product')           user se data lene ke liye
        
        product_id=request.data.get('product')
        
        quantity= int(request.data.get('quantity',1))
        
        #Product.objects.get(id=product_id)    database se data lene ke liye
        #product= Product.objects.get(id=product_id)
        product = get_object_or_404(Product, id=product_id)
        
        # checking ki User जितना मांग रहा है, क्या उतना stock है Iphone ka apni dukaan me ?
        if quantity > product.stock:
            return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)
        
        # ye check krr rha he ki "क्या Dev की cart में iPhone पहले से मौजूद है?"
        cart_item=Cart_item.objects.filter(
            user=request.user,
            product=product
            
        ).first()
        
                # Already exists

        if cart_item:

            cart_item.quantity += quantity

            cart_item.save()

            serializer = CartSerializer(
                cart_item
            )

            return Response(
                serializer.data
            )

        # New item

        cart_item = Cart_item.objects.create(
            user=request.user,
            product=product,
            quantity=quantity
        )

        serializer = CartSerializer(
            cart_item
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
        
            
            
        
        
