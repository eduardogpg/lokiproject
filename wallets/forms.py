import re
from django.forms import ModelForm
from django.forms import CheckboxSelectMultiple
from django.forms import ModelMultipleChoiceField

from django.core.exceptions import ValidationError

from .models import Wallet
from .models import hexadecimal_address_exists

from tokens.models import Token

class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['address', 'alias', 'tokens']
        labels = {'address': 'Dirección', 'alias': 'Alías', 'tokens': 'Tokens'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'address',
            'placeholder': 'Address'
        })

        self.fields['alias'].widget.attrs.update({
            'class': 'form-control',
            'id': 'alias',
            'placeholder': 'Alías'
        })

    tokens = ModelMultipleChoiceField(
        queryset=Token.objects.filter(active=True),
        widget=CheckboxSelectMultiple
    )

    def clean_address(self):
        address = self.cleaned_data['address']

        if hexadecimal_address_exists(address):
            raise ValidationError("Dirección ya se encuentra registrada.")

        if self.is_hexadecimal(address) is None:
            raise ValidationError("Dirección no valida.")
        
        return address


    def is_hexadecimal(self, data):
        return re.fullmatch(r"^(0x|0X)?[a-fA-F0-9]+$", data or "") # BSC validate addresses