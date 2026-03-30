from django import forms
from .models import Tour
from .models import booking


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"


class bookingForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = booking
        fields = "__all__"
