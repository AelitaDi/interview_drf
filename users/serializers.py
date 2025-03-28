from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    """User Login Serializer."""
