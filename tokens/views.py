from django.shortcuts import render
from django.shortcuts import reverse

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from tokens.models import Token

from .forms import TokenForm

class ListTokenView(LoginRequiredMixin, ListView):
    model = Token
    login_url = '/login/'
    template_name = 'tokens/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Token.objects.filter().order_by('-id')


class CreateTokenForm(LoginRequiredMixin, CreateView):
    model = Token
    template_name = 'tokens/create.html'
    login_url = '/login/'
    form_class = TokenForm

    def get_success_url(self):
        return reverse('tokens:list')
