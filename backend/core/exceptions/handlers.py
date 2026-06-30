from rest_framework.views import exception_handler

from core.responses import APIResponse


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return response

    return APIResponse.error(
        message="Validation failed.",
        errors=response.data,
        status_code=response.status_code,
    )