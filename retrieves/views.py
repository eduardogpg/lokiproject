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
    
    transactions = wallet.transaction_set.filter(created_at__gte=datetime.now() - timedelta(days=30)).select_related('token').values(
        'amount', 'block', 'created_at',  'id', 'kind', 'nonce', 'sender', 'status', 'token__symbol'
    )

    return JsonResponse(
        {
            'total': wallet.transaction_set.count(),
            'deposits': wallet.transaction_set.filter(kind='Deposit').count(),
            'balance': wallet.transaction_set.aggregate(Sum('amount')),
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
