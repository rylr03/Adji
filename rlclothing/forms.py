from django.forms import ModelForm
from .models import *
#login
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields =  '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model= Customer
        fields =  '__all__'

class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields =  '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class ApprovalForm(forms.ModelForm):
    class Meta:
        model = OrderApproval
        fields = '__all__'


