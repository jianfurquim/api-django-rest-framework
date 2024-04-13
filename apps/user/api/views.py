from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from apps.user.api.serializers import UserSerializer
from apps.user.models import User


@api_view(["POST"])
def signup(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response(
                {
                    "username": user.username,
                    "user_ref": user.slug,
                    "token": token.key,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"message": "An error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def login(request):
    try:
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token = Token.objects.get(user=user)
        return Response(
            {
                "username": user.username,
                "user_ref": user.slug,
                "token": token.key,
            }
        )
    except Exception as e:
        return Response(
            {"message": "An error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
