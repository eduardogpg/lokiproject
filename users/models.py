from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    receive_emails = models.BooleanField(default=True)
    permision_level = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return self.username

    def admin(self):
        return self.permision_level > 3