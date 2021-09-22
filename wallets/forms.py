import re

from django.forms import Select

from django.forms import ModelForm
from django.forms import CheckboxSelectMultiple
from django.forms import ModelMultipleChoiceField

from django.core.exceptions import ValidationError

from .models import Wallet
from .models import hexadecimal_format
from .models import hexadecimal_address_exists

from tokens.models import Token


class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['address', 'alias', 'tokens']
        labels = {'address': 'Dirección', 'alias': 'Alías', 'tokens': 'Tokens'}

    tokens = ModelMultipleChoiceField(
        queryset=Token.objects.filter(active=True),
        widget=CheckboxSelectMultiple(
            attrs={'class':'ml-1'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'address',
            'placeholder': 'Address'
        })

        self.fields['alias'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'alias',
            'placeholder': 'Alías'
        })


    def clean_address(self):
        address = self.cleaned_data['address']
        
        if self.is_hexadecimal(address) is None:
            raise ValidationError("Dirección no valida.")

        if hexadecimal_address_exists(hexadecimal_format(address)):
            raise ValidationError("La dirección ya se encuentra registrada.")

        return address


    def is_hexadecimal(self, data):
        return re.fullmatch(r"^(0x|0X)?[a-fA-F0-9]+$", data or "") # BSC validate addresses