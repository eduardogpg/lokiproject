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
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'address',
            'placeholder': 'Address'
        })

        self.fields['name'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'name',
            'placeholder': 'Nombre'
        })

        self.fields['symbol'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'symbol',
            'placeholder': 'Símbolo'
        })

        self.fields['active'].widget.attrs.update({
            'class': '',
            'id': 'active',
        })