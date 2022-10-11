from rest_framework import serializers
from users.models.user import User
from users.models.token import Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('access', 'refresh')

        extra_kwargs = {
            'refresh': {'write_only': True},
            'access': {'read_only': True},
        }
