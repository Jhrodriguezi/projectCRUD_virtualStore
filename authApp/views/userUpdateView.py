from rest_framework import generics
from rest_framework.response import Response
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserUpdateView(generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        getId = User.objects.get(pk=id)
        serializer = UserSerializer(instance=getId, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'Message': 'Updated Successfully',
            "username": serializer.data["username"],
            "password": serializer.data["password"],
            "name": serializer.data["name"],
            "email": serializer.data["email"]
        }
        return response
