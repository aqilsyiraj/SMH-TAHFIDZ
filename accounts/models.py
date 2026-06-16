from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [

        ("admin", "Administrator"),

        ("pembina", "Pembina"),

    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="pembina"
    )

    def is_admin(self):

        return self.role == "admin"

    def is_pembina(self):

        return self.role == "pembina"