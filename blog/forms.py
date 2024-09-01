from django import forms
from .models import User, Post


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', "placeholder": 'Enter your name...', "data-sb-validations": 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', "placeholder": 'Enter your email...', "data-sb-validations": 'required,email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', "placeholder": 'Enter your phone number...', "data-sb-validations": 'required'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'id': 'image', "placeholder": 'Enter your photo...'})
        }

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["user","mensage"]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'id': 'name', "placeholder": 'Enter the user...', "data-sb-validations": 'required'}),
            'mensage': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', "placeholder": 'Enter your post here...', "data-sb-validations": 'required', "style": "height: 12rem"})
        }
