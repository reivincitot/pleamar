from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "birth_day",
            "address",
            "phone_number",
            "email",
            "username"
        ]
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        