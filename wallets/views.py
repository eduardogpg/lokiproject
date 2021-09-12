from django.urls import reverse_lazy

from django.shortcuts import reverse
from django.shortcuts import redirect

from django.contrib import messages

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.http import HttpResponseRedirect

from .models import Wallet
from .forms import WalletForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class ListWalletView(LoginRequiredMixin, ListView):
    model = Wallet
    login_url = '/login/'
    template_name = 'wallets/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user).order_by('-id')


class CreateWalletView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Wallet
    template_name = 'wallets/create.html'
    login_url = '/login/'
    form_class = WalletForm
    success_message = "Wallet eactualizada exitosamente"

    def get_success_url(self):
        return reverse('wallets:list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def post(self, request, *args, **kwargs):
        print('Entramos aquí al post')
        return super(CreateWalletView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    def dispatch(self, request, *args, **kwargs):
        print('dispatch!!!')
        return super().dispatch(request, *args, **kwargs)

class WalletDeleteView(DeleteView):
    model = Wallet
    success_url = reverse_lazy('wallets:list')
    

class WalletUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Wallet
    template_name = 'wallets/update.html'
    login_url = '/login/'
    form_class = WalletForm
    success_message = "Wallet eactualizada exitosamente"

    def get_success_url(self):
        return reverse('wallets:list')

