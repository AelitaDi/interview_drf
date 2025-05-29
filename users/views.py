from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserLoginSerializer, UserSelfSerializer, UserUpdateSerializer


class LoginAPIView(TokenObtainPairView):
    """Login."""
    serializer_class = UserLoginSerializer


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """Update profile."""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    lookup_field = 'id'
    lookup_url_kwarg = "id"

    serializer_class = UserUpdateSerializer

    # def get_object(self):
    #     return User.objects.filter(email=self.request.user.email).first()


class UserCreateAPIView(generics.CreateAPIView):
    """Create user."""
    # queryset = User.objects.all()
    serializer_class = UserSelfSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


    # def get_object(self):
    #     # print("wwwwwwwwwwwwwwwwwwwww")
    #     # print(User.objects.filter(email=self.request.user.email).first())
    #     # print("request", self.request)
    #     # print("email", self.request.user.email)
    #     return User.objects.filter(email=self.request.user.email).first()
