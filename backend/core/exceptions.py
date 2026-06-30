from rest_framework.views import exception_handler

from .responses import APIResponse


def custom_exception_handler(exc, context):
    """
    Global Exception Handler
    """

    response = exception_handler(exc, context)

    if response is not None:
        return APIResponse.error(
            message="Validation failed.",
            errors=response.data,
            status_code=response.status_code,
        )

    return response