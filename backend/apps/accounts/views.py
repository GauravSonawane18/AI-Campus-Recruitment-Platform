from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from core.responses import APIResponse

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
)
from .services import AuthenticationService


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = AuthenticationService.register_user(serializer)

        return APIResponse.success(
            message="User registered successfully.",
            data={
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "role": user.role,
            },
            status_code=status.HTTP_201_CREATED,
        )
    

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        auth_data = AuthenticationService.login_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if auth_data is None:
            return APIResponse.error(
                message="Invalid email or password.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return APIResponse.success(
            message="Login successful.",
            data={
                "access": auth_data["access"],
                "refresh": auth_data["refresh"],
                "user": {
                    "id": auth_data["user"].id,
                    "email": auth_data["user"].email,
                    "username": auth_data["user"].username,
                    "role": auth_data["user"].role,
                },
            },
        )    