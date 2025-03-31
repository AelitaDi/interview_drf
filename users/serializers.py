from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    """User Login Serializer."""
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
