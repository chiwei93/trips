from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

required_error_text = "Please ensure that this field is filled."
username_min_error_text = "Please ensure that the username is at least 4 characters long."
password_min_error_text = "Please ensure that the password is at least 8 characters long."


class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=4, error_messages={
        "required": required_error_text,
        "min_length": username_min_error_text
    }, widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'autocomplete': 'off'}))
    email = forms.EmailField(error_messages={
        'required': required_error_text,
        "invalid": "Please enter a valid email address."
    }, widget=forms.EmailInput(attrs={"placeholder": "Enter email address", 'autocomplete': 'off'}))
    password1 = forms.CharField(min_length=8, error_messages={
        'required': required_error_text,
        'min_length': password_min_error_text
    }, widget=forms.PasswordInput(attrs={"placeholder": "Enter password", 'autocomplete': 'off'}))
    password2 = forms.CharField(error_messages={
        'required': required_error_text
    }, widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", 'autocomplete': 'off'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already taken. Please choose another email.')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, error_messages={
        "required": required_error_text,
        "min_length": username_min_error_text
    }, widget=forms.TextInput(attrs={"placeholder": "Enter username", "autocomplete": 'off'}))
    password = forms.CharField(min_length=8, error_messages={
        'required': required_error_text,
        'min_length': password_min_error_text
    }, widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "autocomplete": "off"}))
