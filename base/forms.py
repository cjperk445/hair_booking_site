from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.save()
        return user
