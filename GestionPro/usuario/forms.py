__author__ = 'rvidal'

from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Usuario

class FormUsuario(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = Usuario
        fields = ('username','email', 'is_superuser','first_name', 'last_name', 'cedula','celular', 'direccion')



class FormUsuarioChange(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Usuario
        fields = ('email', 'is_superuser','first_name', 'last_name','celular', 'direccion')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ModelForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user