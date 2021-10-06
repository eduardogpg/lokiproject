from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import post_save

from Web3API.abis import abi
from Web3API.abis import total_supply

class Token(models.Model):
    address = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    symbol = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    abi = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=500, blank=True, null=True, default='')
    supply = models.BigIntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.symbol}"


    def set_abi(self):
        if self.abi:
            return self.abi

        response = abi(self)
        if response:
            self.abi = str(response)
            self.save()

        return self.abi

    def set_total_supply(self):
        if self.supply:
            return self.supply
        
        self.supply = total_supply(self)
        self.save()


def set_abi(sender, instance, *args, **kwargs):
    instance.set_abi()


def set_total_supply(sender, instance, created, raw, using, update_fields, *args, **kwargs):
    instance.set_total_supply()


pre_save.connect(set_abi, sender=Token)
# post_save.connect(set_total_supply, sender=Token)