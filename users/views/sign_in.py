from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from users.models.user import User
from users.models.token import Token
from users.serializers.user import UserInSerializer, UserSerializer
from django.contrib.auth import authenticate


class SignInView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserInSerializer)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            token = Token.objects.filter(user = user)
            if token.exists():
                token.delete()

            token = Token.objects.create(user = user)
            serializer = UserSerializer(user)
            return Response({
                "user": serializer.data,
                "token": {
                    "access": token.access,
                    "refresh": token.refresh,
                }
            }, 200)
        return Response({
            "error": "User not found!",
        }, 401)
