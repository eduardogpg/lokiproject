from django.db import models

class Block(models.Model):
    block_id = models.IntegerField(null=False, blank=False)
    transactions = models.IntegerField(null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
