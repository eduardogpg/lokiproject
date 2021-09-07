from django.db import models

class Token(models.Model):
    address = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    symbol = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.symbol}"
