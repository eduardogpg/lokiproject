import json

from datetime import datetime
from datetime import timedelta

from django.db.models import Sum

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from wallets.models import Wallet
from transactions.models import Transaction


@login_required(login_url='/login')
def dashboard(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk)
    
    transactions = wallet.transaction_set.filter(created_at__gte= datetime.now() - timedelta(days=30)).values(
        'block', 'wallet', 'amount', 'token', 'kind', 'sender', 'created_at'
    )

    return JsonResponse(
        {
            'total': wallet.transaction_set.count(),
            'deposits': wallet.transaction_set.filter(kind='Deposit').count(),
            'balance': wallet.transaction_set.annotate(Sum('amount'))[0].amount__sum,
            'transactions': list(transactions)
        }
    )


@login_required(login_url='/login')
def wallets(request):

    return JsonResponse(
        {
            'wallets': list(
                request.user.wallet_set.all().values('id', 'hexadecimal', 'alias')
            )
        }
    )
