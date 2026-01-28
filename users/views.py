from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status 
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer ,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User ,OTP
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MeSerializer
from core.utils import generate_otp
 

class RegisterView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "token": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "phone": user.phone,
                    "role": user.role,
                    "language": user.language,
                },
            },
            status=status.HTTP_201_CREATED,
        )




class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_class = LoginSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response({
            "token": str(refresh.access_token)
        })



# class MeView(GenericAPIView):
#     serializer_class = MeSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = self.get_serializer(request.user)
#         return Response(serializer.data)
    

class MeView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "language": user.language,
            "created_at": user.created_at,
        })