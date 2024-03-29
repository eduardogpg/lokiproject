from django.forms import ModelForm

from .models import Token

class TokenForm(ModelForm):
    class Meta:
        model = Token
        fields = ['address', 'name', 'symbol', 'image', 'active', 'total', 'coingecko_id']
        labels = {'address': 'Dirección', 'name': 'Nombre', 'symbol': 'Símbolo', 'image': 'Imagen', 'active': 'Activo'}

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


        self.fields['image'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'image',
            'placeholder': 'Imagen'
        })

        self.fields['total'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'total',
            'placeholder': 'Cantidad por la cual se hará la división'
        })

        self.fields['coingecko_id'].widget.attrs.update({
            'class': 'appearance-none block w-full py-3 px-4 leading-tight text-gray-700 bg-gray-50 focus:bg-white border border-gray-200 focus:border-gray-500 rounded focus:outline-none',
            'id': 'tocoingecko_idtal',
            'placeholder': 'Id de CoinGecko'
        })

        self.fields['active'].label = "Estatus Activo"