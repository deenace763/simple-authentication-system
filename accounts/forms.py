from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label="Full Name",
        help_text=None
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=None
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text=None
    )

    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        help_text=None
    )

    email = forms.EmailField(
        required=True,
        label="Email address",
        help_text=None
    )

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
