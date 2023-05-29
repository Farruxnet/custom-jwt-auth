from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from users.serializers.user import UserSerializer
from django.contrib.auth.hashers import make_password


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(password=make_password(request.data['password']))
        return Response(serializer.data, 201)
