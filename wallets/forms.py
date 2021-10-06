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

    def clean_address(self):
        address = self.cleaned_data['address']
        
        if self.is_hexadecimal(address) is None:
            raise ValidationError("Dirección no valida.")

        if hexadecimal_address_exists(hexadecimal_format(address)):
            raise ValidationError("La dirección ya se encuentra registrada.")

        return address


    def is_hexadecimal(self, data):
        return re.fullmatch(r"^(0x|0X)?[a-fA-F0-9]+$", data or "") # BSC validate addresses


class WalletCreateForm(WalletForm):
    class Meta:
        model = Wallet
        fields = ['address', 'alias', 'tokens', 'default']
        labels = {'address': 'Dirección', 'alias': 'Alías', 'tokens': 'Tokens', 'default': 'default'}


    tokens = ModelMultipleChoiceField(
        queryset=None,
        widget=CheckboxSelectMultiple
    )


    def __init__(self, disabled=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({
            'class': 'block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'address',
            'placeholder': 'Address'
        })

        self.fields['address'].disabled = disabled

        self.fields['alias'].widget.attrs.update({
            'class': 'block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'alias',
            'placeholder': 'Alías'
        })

        self.fields['tokens'].queryset = Token.objects.filter(active=True)
        self.fields['tokens'].widget.attrs.update(
            { 'class':'ml-1' }
        )

        self.fields['default'].widget.attrs.update(
            { 'class':'mt-1' }
        )
        self.fields['default'].label = "Billetera principal"


class WalletUpdateForm(WalletForm):
    class Meta:
        model = Wallet
        fields = ['alias', 'tokens', 'default' ]
        labels = {'alias': 'Alías', 'tokens': 'Tokens', 'default': 'Billetera principal'}

    tokens = ModelMultipleChoiceField(
        queryset=None,
        widget=CheckboxSelectMultiple
    )

    def __init__(self, disabled=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['alias'].widget.attrs.update({
            'class': 'block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'alias',
            'placeholder': 'Alías'
        })

        self.fields['tokens'].queryset = Token.objects.filter(active=True)
        self.fields['tokens'].widget.attrs.update(
            { 'class':'ml-1' }
        )

        self.fields['default'].label = "Billetera principal"

    