from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email    = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=300)

    