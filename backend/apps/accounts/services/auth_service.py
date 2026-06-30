from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from core.base.service import BaseService


class AuthenticationService(BaseService):
    @staticmethod
    def register_user(serializer):
        return AuthenticationService.execute(serializer.save)

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
    

    @staticmethod
    def logout_user(refresh_token):
        """
        Blacklist the refresh token.
        """

        token = RefreshToken(refresh_token)
        token.blacklist()

        return True