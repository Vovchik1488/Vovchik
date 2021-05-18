from django import forms
from secondapp.models import Order, Pizza

class OrderForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ('pizza', 'name', 'phone')