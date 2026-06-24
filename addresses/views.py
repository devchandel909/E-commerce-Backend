from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Address
from .serializers import AddressSerializer



class AddressView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = AddressSerializer(
            data=request.data
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

        queryset = Address.objects.filter(
            user=request.user
        )

        serializer = AddressSerializer(
            queryset,
            many=True
        )

        return Response(
            serializer.data
        )
    
class AddressUpdateView(UpdateAPIView):

    

        serializer_class = (
            AddressSerializer
        )

        permission_classes = [
            IsAuthenticated
        ]

        def get_queryset(self):

            return Address.objects.filter(
                user=self.request.user
            )
            
class AddressDeleteView(DestroyAPIView):

        serializer_class = (
            AddressSerializer
        )

        permission_classes = [
            IsAuthenticated
        ]

        def get_queryset(self):

            return Address.objects.filter(
                user=self.request.user
            )