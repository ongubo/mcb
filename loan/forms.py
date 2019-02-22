from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Loan


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class LoanForm(forms.ModelForm):
    purpose = forms.CharField(
        label='Loan Purpose', max_length=500, required=True, widget=forms.TextInput(attrs={'placeholder': 'Loan Purpose'}))
    amount_requested = forms.DecimalField(
        label=0, required=True, widget=forms.TextInput(attrs={'placeholder': 'Amount'}))

    class Meta:
        model = Loan
        fields = ['purpose', 'amount_requested']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'membership_number',
            'first_name',
            'last_name',
            'middle_name',
            # 'id_number',
            # 'dob',
            'home_address',
            'office_phone',
            'mobile_phone',
            # 'pin_number',
            # 'email'
        ]
