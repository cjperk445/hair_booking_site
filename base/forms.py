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
    '''
    This Meta class constructs booking form from the model
    '''
    class Meta:
        '''
        This add form inputs from items within the model
        they should appear as form fields
        '''
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

        #widget used to put dropdown calendar in form

        self.fields['date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'min': datetime.date.today().isoformat(),  # disables past dates
            'id': 'id_date',
            'class': 'form-control'
        })

        # Add time picker widget
        self.fields['time'].widget = forms.TimeInput(attrs={
            'type': 'time',
            'id': 'id_time',
            'class': 'form-control',
            '''
            Limit the time choices to every fifteen mins, i.e on the hour 
            quarter past, half past and quarter too. The time is represented
            in seconds 900 seconds = fifteen minutes
            '''
            'step':900,
        })

    '''
    The Below Clean function is used to ensure all the information put in the
    booking form matches the paramaters it should.
    The function will check for correct date selection (if the salon is open)
    and correct opening times.
    Also There is a check that the chosen stylist offers the chosen
    service
    '''

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        stylist = cleaned_data.get('stylist')
        service = cleaned_data.get('service')

        if not date or not time:
            return cleaned_data

        # This will map weekday numbers to names
        weekday = date.weekday()  # Monday = 0, Sunday = 6

        # This defines the hours the salon is open
        salon_hours = {
            1: (datetime.time(9, 0), datetime.time(14, 30)),  # Tuesday
            2: (datetime.time(9, 0), datetime.time(19, 0)),   # Wednesday
            3: (datetime.time(9, 0), datetime.time(19, 0)),   # Thursday
            4: (datetime.time(9, 0), datetime.time(18, 0)),   # Friday
            5: (datetime.time(9, 0), datetime.time(17, 0)),   # Saturday
        }

        # Date Check - is the salon open?

        if weekday not in salon_hours:
            self.add_error('date', "Sorry, the salon is closed on that day.")
            return cleaned_data
        
        # time check - is the salon open during that time?

        open_time, close_time = salon_hours[weekday]
        if time < open_time or time > close_time:
            self.add_error('time', f"We're open from {open_time.strftime('%H:%M')} to {close_time.strftime('%H:%M')} on that day. Please choose a time within that range.")

        # Stylist service check

        if stylist and service:
            if not stylist.services.filter(id=service.id).exists():
                self.add_error('service', f"Sorry {stylist}, doesn't offer that service. Please Choose another service")

        return cleaned_data




