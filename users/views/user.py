from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from users.models.user import User
from users.serializers.user import UserUpdateSerializer


class UserUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserUpdateSerializer

    @swagger_auto_schema(request_body=UserUpdateSerializer)
    def put(self, request, *args, **kwargs):
        data = request.data
        qs = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(qs, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        return Response(serializer.errors, 400)
