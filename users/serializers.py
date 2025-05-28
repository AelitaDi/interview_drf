from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from forest.serializers import TreeSerializer
from users.models import User


class UserLoginSerializer(TokenObtainPairSerializer):
    """User Login Serializer."""
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)


class UserSelfSerializer(ModelSerializer):
    """User serializer for register and update."""
    trees = TreeSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = "__all__"
