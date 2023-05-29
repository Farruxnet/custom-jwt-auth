from rest_framework import serializers
from users.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone_number')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
        }


class UserInSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, trim_whitespace=True)
    password = serializers.CharField(required=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ('username', 'password')
