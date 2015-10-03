from .models import Event
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'location', 'attendees', 'voting_options', 'start_date', 'end_date')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

