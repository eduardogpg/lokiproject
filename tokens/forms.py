from django.forms import ModelForm

from .models import Token

class TokenForm(ModelForm):
    class Meta:
        model = Token
        fields = ['address', 'name', 'symbol', 'active']
        labels = {'address': 'Dirección', 'name': 'Nombre', 'symbol': 'Símbolo', 'active': 'Activo'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'address',
            'placeholder': 'Address'
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Nombre'
        })

        self.fields['symbol'].widget.attrs.update({
            'class': 'form-control',
            'id': 'symbol',
            'placeholder': 'Símbolo'
        })
