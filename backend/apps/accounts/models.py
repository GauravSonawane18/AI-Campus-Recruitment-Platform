from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for the AI Campus Recruitment Platform.
    """

    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        RECRUITER = "RECRUITER", "Recruiter"
        TPO = "TPO", "Placement Officer"
        ADMIN = "ADMIN", "Admin"

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email} ({self.role})"