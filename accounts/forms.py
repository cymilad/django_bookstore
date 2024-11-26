from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', 'email',)
        fields = ['username', 'email', 'first_name', 'last_name', 'age']
        labels = {
            'username': 'Enter Username :',
            'email': 'Enter Email :',
            'first_name': 'Enter First Name :',
            'last_name': 'Enter Last Name :',
            'age': 'Enter Age :',
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'email', 'first_name', 'last_name', 'age']
        labels = {
            'username': 'Enter Username :',
            'email': 'Enter Email :',
            'first_name': 'Enter First Name :',
            'last_name': 'Enter Last Name :',
            'age': 'Enter Age :',
        }