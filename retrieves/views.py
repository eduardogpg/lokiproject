import json

from datetime import datetime
from datetime import timedelta

from django.db.models import Sum

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from tokens.models import Token
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


def generate_token(wallet, token, prices):
    token_dict = dict(symbol=token.symbol, image=token.image)

    balance = total_balance_of(token, wallet) / token.total
    balance = round(balance, 4)
    price = prices[token.coingecko_id]['usd']

    token_dict['balance'] = balance
    token_dict['price'] = price
    token_dict['total'] = round(balance * price, 4)

    return token_dict


@login_required(login_url='/login')
def balance(request, pk):
    
    wallet = get_object_or_404(Wallet, pk=pk)
    tokens = Token.objects.filter(wallettokens__wallet_id=wallet.id)

    coingecko_ids = ','.join([ token.coingecko_id for token in tokens ])
    prices = get_prices(coingecko_ids)
    
    return JsonResponse(
        {
            'tokens': [ generate_token(wallet, token, prices) for token in tokens ]
        }
    )