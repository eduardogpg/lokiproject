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

from Web3API.tokens import get_prices
from Web3API.wallets import total_balance_of

@login_required(login_url='/login')
def dashboard(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk)
    
    transactions = wallet.transaction_set.filter(created_at__gte=datetime.now() - timedelta(days=30)).select_related('token').values(
        'amount', 'block', 'created_at', 'token__image', 'id', 'kind', 'nonce', 'sender', 'status', 'token__symbol'
    )
    balance = wallet.transaction_set.aggregate(Sum('amount'))

    return JsonResponse(
        {
            'total': wallet.transaction_set.count(),
            'deposits': wallet.transaction_set.filter(kind='Deposit').count(),
            'balance': balance['amount__sum'] if balance['amount__sum'] else 0,
            'transactions': list(transactions)
        }
    )


@login_required(login_url='/login')
def wallets(request):
    return JsonResponse(
        {
            'wallets': list(
                Wallet.objects.filter(user=request.user).values('hexadecimal', 'alias', 'id', 'default').order_by('-default')
            )
        }
    )


@login_required(login_url='/login')
def balance(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk)

    tokens = list()
    ids = [ wallet['token__coingecko_id'] for wallet in wallet.wallettokens_set.all().values('token__coingecko_id')]

    prices = get_prices(ids)
    

    for token in wallet.wallettokens_set.all().values('token__address', 'token__abi', 'token__symbol', 'token__image', 'token__total', 'token__coingecko_id'):
        current_token = dict()

        current_token['symbol'] = token['token__symbol']
        current_token['image'] = token['token__image']

        balance = total_balance_of(token['token__address'], token['token__abi'], wallet.address)
        balance = balance / token['token__total']

        current_token['balance'] = float("{:.4f}".format(round(balance, 4)))

        current_token['price'] = prices[token['token__coingecko_id']]['usd']

        total = current_token['balance'] * current_token['price']
        current_token['total'] = float("{:.4f}".format(round(total, 4)))

        tokens.append(current_token)

    return JsonResponse(
        {
            'tokens': tokens
        }
    )