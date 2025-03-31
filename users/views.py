from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import UserLoginSerializer


class LoginAPIView(TokenObtainPairView):
    """Login."""
    serializer_class = UserLoginSerializer


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """Update profile."""
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    serializer_class = ...
