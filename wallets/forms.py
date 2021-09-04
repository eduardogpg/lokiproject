import re
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Wallet
from .models import hexadecimal_address_exists

class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['address']
        labels = {'address': 'Dirección'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'address',
            'placeholder': 'Address'
        })

    def clean_address(self):
        address = self.cleaned_data['address']

        if hexadecimal_address_exists(address):
            raise ValidationError("Dirección ya se encuentra registrada.")

        if self.is_hexadecimal(address) is None:
            raise ValidationError("Dirección no valida.")
        
        return address


    def is_hexadecimal(self, data):
        return re.fullmatch(r"^(0x|0X)?[a-fA-F0-9]+$", data or "") # BSC validate addresses