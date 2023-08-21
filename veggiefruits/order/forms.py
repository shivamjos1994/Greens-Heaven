from django import forms
from .models import Checkout

PAYMENT_CHOICES = [
    ('online', 'Online'),
    ('cash on delivery', 'Cash on delivery'),
]


class CheckoutForm(forms.ModelForm):
    favorite_fruit = forms.CharField(label='Mode of Payment:',
                                     widget=forms.RadioSelect(choices=PAYMENT_CHOICES))
    class Meta:
        model = Checkout
        fields = ('address','email','invoice_no')
