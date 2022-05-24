from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    model = User
    fields = ['username', 'email', 'password1', 'password2']