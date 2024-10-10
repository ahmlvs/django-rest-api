from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer



@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_user(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
