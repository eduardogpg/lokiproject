from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    receive_emails = models.BooleanField(default=True)

    def __str__(self):
        return self.username