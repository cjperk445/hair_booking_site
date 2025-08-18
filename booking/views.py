from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.forms import BookingForm

# Create your views here.


def booking(request):
    return render(request, "booking/booking.html",
                  )

def booking_success(request):
    return render(request, "booking/booking_success.html")

@login_required
def create_booking(request):
    '''
    This will allow user to create a booking and
    add it to the database
    '''
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            return redirect('booking_success')

    else:
        form = BookingForm(user=request.user)

    return render(request, 'booking/booking.html', {'form': form})