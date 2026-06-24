from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (

    RegisterSerializer,

    ProfileSerializer,

    ChangePasswordSerializer
)

User = get_user_model()


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
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
        
        
        
        
        
class LoginView(APIView):

    def post(self, request):

        username = request.data.get(
            'username'
        )

        password = request.data.get(
            'password'
        )

        from django.contrib.auth import authenticate

        user = authenticate(

            username=username,

            password=password
        )

        if not user:

            return Response(

                {
                    'error':
                    'Invalid Credentials'
                },

                status=400
            )

        refresh = RefreshToken.for_user(
            user
        )

        return Response({

            'refresh':
            str(refresh),

            'access':
            str(refresh.access_token)
        })


class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        serializer = ProfileSerializer(
            request.user
        )

        return Response(
            serializer.data
        )

    def put(self, request):

        serializer = ProfileSerializer(

            request.user,

            data=request.data,

            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=400
        )
        
        
class ChangePasswordView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = (
            ChangePasswordSerializer(
                data=request.data
            )
        )

        if serializer.is_valid():

            if not request.user.check_password(

                serializer.validated_data[
                    'old_password'
                ]
            ):

                return Response({

                    'error':
                    'Wrong Password'
                })

            request.user.set_password(

                serializer.validated_data[
                    'new_password'
                ]
            )

            request.user.save()

            return Response({

                'message':
                'Password Changed'
            })

        return Response(
            serializer.errors,
            status=400
        )