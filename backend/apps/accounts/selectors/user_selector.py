from django.contrib.auth import get_user_model

from core.base.selector import BaseSelector

User = get_user_model()


class UserSelector(BaseSelector):
    """
    User read operations.
    """

    model = User

    @classmethod
    def get_by_email(cls, email):
        return cls.filter(email=email).first()

    @classmethod
    def get_by_username(cls, username):
        return cls.filter(username=username).first()

    @classmethod
    def email_exists(cls, email):
        return cls.exists(email=email)