from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        data = request.data.copy()

        data['user'] = request.user.id

        serializer = WishlistSerializer(
            data=data
        )

        if serializer.is_valid():

            serializer.save(
                user=request.user
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):

        queryset = Wishlist.objects.filter(
            user=request.user
        )

        serializer = WishlistSerializer(
            queryset,
            many=True
        )

        return Response(
            serializer.data
        )


class WishlistDeleteView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        product_id
    ):

        wishlist_item = Wishlist.objects.filter(
            user=request.user,
            product_id=product_id
        ).first()

        if not wishlist_item:

            return Response(
                {
                    "error": "Product not in wishlist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        wishlist_item.delete()

        return Response(
            {
                "message": "Removed successfully"
            },
            status=status.HTTP_200_OK
        )