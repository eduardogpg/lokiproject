from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from tokens.models import Token

from .forms import TokenForm

from users.decorators import admin_validator

from django.urls import reverse_lazy

class TokenDeleteView(LoginRequiredMixin, DeleteView):
    model = Token
    success_url = reverse_lazy('tokens:list')

    @method_decorator(admin_validator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ListTokenView(LoginRequiredMixin, ListView):
    model = Token
    login_url = '/login/'
    template_name = 'tokens/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get_queryset(self):
        return Token.objects.filter().order_by('-id')


    @method_decorator(admin_validator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CreateTokenForm(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Token
    template_name = 'tokens/create.html'
    login_url = '/login/'
    form_class = TokenForm
    success_message = 'Token registrado existosamente'

    def get_success_url(self):
        return reverse('tokens:list')


    @method_decorator(admin_validator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UpdateTokenView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Token
    login_url = '/login/'
    template_name = 'tokens/update.html'
    form_class = TokenForm
    success_message = 'Token actualizado existosamente'


    def get_success_url(self):
        return reverse('tokens:list')


    @method_decorator(admin_validator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TokenDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Token
    login_url = '/login/'
    template_name = 'tokens/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def abi(request, pk):
    token = get_object_or_404(Token, pk=pk)
    
    token.set_abi()
    token.set_total_supply()

    return redirect('tokens:list')