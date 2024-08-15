from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update({'placeholder': 'senha'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail'})
        self.fields['username'].widget.attrs.update({'placeholder': 'usuário'})
        
    def verificaçao():
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ja existe")
        return email