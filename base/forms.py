from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import gettext
from .models import Booking, Service, User
import datetime


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields["email"].label = gettext("Email")

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'stylist', 'date', 'time']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        # this is the person logged in

        super().__init__(*args, **kwargs)

        # This will only show the stylists, if they;re labelled as Staff

        self.fields['stylist'].queryset = User.objects.filter(is_staff=True)
        # the below should only show what the stylist offers
        self.fields['service'].queryset = Service.objects.all()
    
    