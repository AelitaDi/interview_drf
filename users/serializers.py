from typing import Any

from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from forest.serializers import TreeSerializer
from users.models import User, UserProfile


class UserLoginSerializer(TokenObtainPairSerializer):
    """User Login Serializer."""
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        data = {}
        email = attrs.get("email")
        self.user = User.objects.filter(Q(email=email) | Q(username=email)).first()
        print(self.user)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        print(attrs)

        return data


class UserSelfSerializer(ModelSerializer):
    """User serializer for register and update."""
    trees = TreeSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = "__all__"


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Profile Update Serializer."""

    class Meta:
        model = UserProfile
        fields = ['address']


class UserUpdateSerializer(serializers.ModelSerializer):
    """User Update Serializer."""
    profile = ProfileUpdateSerializer()
    # id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["email", "username", "profile", "id"]

    def update(self, instance, validated_data):
        instance = self.request.user
        return super().update(instance, validated_data)
