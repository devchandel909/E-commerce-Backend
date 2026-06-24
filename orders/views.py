from decimal import Decimal
from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cart.models import Cart_item
from addresses.models import Address
from .models import Order, OrderItem
from .serializers import OrderSerializer


class CreateOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        address_id = request.data.get('address')

        address = get_object_or_404(
            Address,
            id=address_id,
            user=request.user
        )

        cart_items = Cart_item.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response(
                {'error': 'Cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔥 Atomic transaction (ALL OR NOTHING)
        with transaction.atomic():

            total = Decimal('0')

            # Stock validation FIRST (important)
            for item in cart_items:
                if item.quantity > item.product.stock:
                    return Response(
                        {
                            "error": f"Not enough stock for {item.product.name}"
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Calculate total
            for item in cart_items:
                total += item.product.price * item.quantity

            # Create Order
            order = Order.objects.create(
                user=request.user,
                address=address,
                total_amount=total
            )

            # Create OrderItems + reduce stock
            for item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

                item.product.stock -= item.quantity
                item.product.save()

            # Clear cart
            cart_items.delete()

        serializer = OrderSerializer(order)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )