# forms.py
from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .models import User, ImageEntry


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

# para manejar la creación y actualización de ImageEntry.
class ImageEntryForm(forms.ModelForm):
    class Meta:
        model = ImageEntry
        fields = ['title', 'image', 'description', 'materials', 'date', 'author']