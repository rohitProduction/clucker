from django import forms
from .models import User, Post

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio']
        widgets = { 'bio': forms.Textarea() }

    new_password = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    password_confirmation = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput())


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
