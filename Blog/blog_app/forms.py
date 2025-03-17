from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label = "Confirm Password")


class AddPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content']
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your content here'})
    )   

class PasswordChangeFormCustom(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = "Enter old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = "Enter new Password")
    confirm_password  = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = "Enter confirm Password")
class SimplePasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label = "Enter your email")

class ForgotPasswordSendingForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = "Enter new Password")
    confirm_password  = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = "Enter confirm Password")