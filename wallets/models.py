from django.db import models
from users.models import User
from tokens.models import Token

from django.core.exceptions import ValidationError

from django.db.models.signals import pre_save
from django.db.models.signals import post_save

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hexadecimal = models.CharField(max_length=254, null=False, blank=False) # Hexadecimal is the field without prefix 0x
    address = models.CharField(max_length=254, null=False, blank=False)
    alias = models.CharField(max_length=100, null=False, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    tokens = models.ManyToManyField(Token, through='wallet_tokens.WalletTokens')
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.hexadecimal


def hexadecimal_format(address):
    return address.lower()[2:] # Remove prefix


def hexadecimal_address_exists(hexadecimal):
    hexadecimal = hexadecimal.lower()
    return Wallet.objects.filter(hexadecimal=hexadecimal).exclude(hexadecimal=hexadecimal).exists()

"""
def validate_if_address_exists(sender, instance, *args, **kwargs):
    if address_exists(instance.address):
        raise ValidationError('La dirección ya se encuentra registrada!')
"""

def set_wallet_format(sender, instance, *args, **kwargs):
    instance.hexadecimal = hexadecimal_format(instance.address)


def check_default(sender, instance, created, *args, **kwargs):
    if instance.default == False and Wallet.objects.filter(user=instance.user).filter(default=True).exists() == False:
        instance.default = True
        instance.save()

def update_default(sender, instance, created, *args, **kwargs):
    if instance.default:
        
        for wallet in Wallet.objects.filter(user=instance.user).exclude(pk=instance.pk):
            wallet.default = False
            wallet.save()


pre_save.connect(set_wallet_format, sender=Wallet)

post_save.connect(check_default, sender=Wallet)
post_save.connect(update_default, sender=Wallet)