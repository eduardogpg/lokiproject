from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Transaction

class TransactionDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Transaction
    login_url = '/login/'
    template_name = 'transactions/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['token'] = self.get_object().token
        return context