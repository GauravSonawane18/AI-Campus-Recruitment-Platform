from rest_framework.response import Response


class APIResponse:
    """
    Standard API response format for the entire project.
    """

    @staticmethod
    def success(
        message="Success",
        data=None,
        status_code=200,
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
        message="Validation failed.",
        errors=None,
        status_code=400,
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