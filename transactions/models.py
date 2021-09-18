from django.db import models
from wallets.models import Wallet
from tokens.models import Token

from django.db.models.signals import pre_save

class Transaction(models.Model):
    hash = models.CharField(max_length=255, null=False, blank=False)
    block = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False, default=0)
    status = models.CharField(max_length=20, null=True, blank=True)
    kind = models.CharField(max_length=20, null=True, blank=True)
    sender = models.CharField(max_length=255, null=False, blank=False)
    token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, blank=True)
    nonce = models.IntegerField(null=False, blank=False)
    input = models.CharField(max_length=255, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.token}"
