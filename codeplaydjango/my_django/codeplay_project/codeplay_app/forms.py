from django import forms
from .models import Pendaftaran  
class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        fields = ['name', 'age', 'email', 'password', 'kelas']  
        widgets = {
            'password': forms.PasswordInput(),  
        }


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
