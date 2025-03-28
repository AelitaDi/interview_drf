from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginAPIView(TokenObtainPairView):
    """Login."""


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """Update profile."""
