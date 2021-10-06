
from django.urls import reverse_lazy


from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib import messages

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.http import HttpResponseRedirect

from django.core.serializers import serialize

from .models import Wallet

from .forms import WalletCreateForm
from .forms import WalletUpdateForm

from tokens.models import Token
from transactions.models import Transaction
from wallet_tokens.models import WalletTokens

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from Web3API.wallets import total_balance_of

@login_required(login_url='/login')
def dashboard(request):
    if Wallet.objects.filter(user=request.user).exists():

        wallet = Wallet.objects.filter(user=request.user).filter(default=True).first()
        
        return render(request, 'wallets/dashboard.html', {
            'wallet': wallet,

        })

    else:
        return redirect('wallets:admin')


@login_required(login_url='/login')
def admin(request):
    
    if Wallet.objects.filter(user_id=request.user.id).exists():
        return redirect('wallets:dashboard')

    return render(request, 'wallets/admin.html', {})


class CreateWalletView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Wallet
    template_name = 'wallets/create.html'
    login_url = '/login/'
    form_class = WalletCreateForm
    success_message = "Wallet eactualizada exitosamente"

    def get_success_url(self):
        return reverse('wallets:dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['form'] = WalletCreateForm(
            initial={
                'default': not Wallet.objects.filter(user=self.request.user).exists()
            }
        )
        
        return context

    def post(self, request, *args, **kwargs):
        return super(CreateWalletView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class WalletDeleteView(DeleteView):
    model = Wallet
    success_url = reverse_lazy('wallets:list')
    

class WalletUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Wallet
    template_name = 'wallets/update.html'
    login_url = '/login/'
    form_class = WalletUpdateForm
    success_message = "Wallet actualizada exitosamente"

    def get_success_url(self):
        return reverse('wallets:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tokens'] = [ wt['token_id'] for wt in WalletTokens.objects.filter(wallet_id=self.get_object().id).values('token_id')]
        return context

