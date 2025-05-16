from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser,Patient,Staff


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'phone_user','password1','password2')

class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('polis_num',)

class StaffSignUpForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('position',)

