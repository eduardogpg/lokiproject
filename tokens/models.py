from django.db import models
from django.db.models.signals import pre_save

from Web3API.abis import abi

class Token(models.Model):
    address = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    symbol = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    abi = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.symbol}"


    def set_abi(self):
        if self.abi:
            return None

        response = abi(self.address)
        if response:
            self.abi = str(response)
            self.save()

        return self.abi
"""
def set_abi(sender, instance, *args, **kwargs):
    instance.set_abi()
"""

# pre_save.connect(set_abi, sender=Token)