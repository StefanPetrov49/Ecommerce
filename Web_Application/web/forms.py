from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from Web_Application.web.models import Customer, ShippingAddress


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditCustomerForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']


class DeleteCustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']


class CreateShippingAddress(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city']
