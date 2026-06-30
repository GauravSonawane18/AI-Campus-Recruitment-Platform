from rest_framework.response import Response
from rest_framework import status


class APIResponse:
    """
    Standard API Response Format
    """

    @staticmethod
    def success(
        message="Success",
        data=None,
        status_code=status.HTTP_200_OK,
    ):
        return Response(
            {
                "success": True,
                "message": message,
                "data": data,
                "errors": None,
            },
            status=status_code,
        )

    @staticmethod
    def error(
        message="Error",
        errors=None,
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        return Response(
            {
                "success": False,
                "message": message,
                "data": None,
                "errors": errors,
            },
            status=status_code,
        )