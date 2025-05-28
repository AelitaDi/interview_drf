from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserLoginSerializer, UserSelfSerializer


class LoginAPIView(TokenObtainPairView):
    """Login."""
    serializer_class = UserLoginSerializer


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """Update profile."""
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    serializer_class = UserSelfSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Create user."""
    queryset = User.objects.all()
    serializer_class = UserSelfSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
