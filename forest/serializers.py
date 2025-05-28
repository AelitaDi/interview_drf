from rest_framework import serializers

from forest.models import Tree
from users.models import User


class UserTreeSerializer(serializers.ModelSerializer):
    """User serializer for trees."""

    class Meta:
        model = User
        fields = ("email",)


class AdminTreeSerializer(serializers.ModelSerializer):
    """Serializer for trees with owner."""

    owner = UserTreeSerializer(read_only=True)

    class Meta:
        model = Tree
        fields = "__all__"


class TreeSerializer(serializers.ModelSerializer):
    """Serializer for trees."""

    class Meta:
        model = Tree
        fields = ("name", "type_of_tree", "created_at")


class TreeCreateSerializer(serializers.ModelSerializer):
    """Serializer for trees."""

    class Meta:
        model = Tree
        fields = ("type_of_tree",)
