from django.db import transaction


class BaseService:
    """
    Base service class.

    All business logic services should inherit from this class.
    """

    @staticmethod
    def atomic():
        """
        Shortcut for database transaction.atomic.
        """
        return transaction.atomic()

    @staticmethod
    def execute(callback, *args, **kwargs):
        """
        Execute a service callback inside an atomic transaction.
        """
        with transaction.atomic():
            return callback(*args, **kwargs)