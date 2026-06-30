from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationService:
    @staticmethod
    def register_user(serializer):
        return serializer.save()

    @staticmethod
    def login_user(email, password):
        """
        Authenticate the user and generate JWT tokens.
        """

        user = authenticate(
            username=email,
            password=password,
        )

        if user is None:
            return None

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }