from django.urls import reverse_lazy

from django.shortcuts import reverse

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect

from .models import Wallet
from .forms import WalletForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ListWalletView(LoginRequiredMixin, ListView):
    model = Wallet
    login_url = '/login/'
    template_name = 'wallets/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user).order_by('-id')


class CreateWalletView(LoginRequiredMixin, CreateView):
    model = Wallet
    template_name = 'wallets/create.html'
    login_url = '/login/'
    form_class = WalletForm

    def get_success_url(self):
        return reverse('wallets:list')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class WalletDeleteView(DeleteView):
    model = Wallet
    success_url = reverse_lazy('wallets:list')
    