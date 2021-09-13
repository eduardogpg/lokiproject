from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    receive_emails = models.BooleanField(default=True)
    permission_level = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return self.username

    def admin(self):
        return self.permission_level > 3