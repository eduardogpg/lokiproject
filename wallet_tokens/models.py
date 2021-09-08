from django.db import models

from wallets.models import Wallet
from tokens.models import Token

class WalletTokens(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, null=True, blank=True)


