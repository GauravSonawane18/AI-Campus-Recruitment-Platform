from rest_framework.views import APIView


class BaseAPIView(APIView):
    """
    Base API View.

    Every API in the project should inherit from this class.
    Common behaviors such as authentication, permissions,
    throttling, logging, and auditing will be centralized here.
    """

    authentication_classes = APIView.authentication_classes
    permission_classes = APIView.permission_classes
    throttle_classes = APIView.throttle_classes

    def get_serializer(self, serializer_class, *args, **kwargs):
        """
        Return serializer instance.
        """
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        """
        Common serializer context.
        """
        return {
            "request": self.request,
            "view": self,
        }