from .models import Event, VotingOption
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class FileInput(forms.FileInput):
    input_type = 'file'

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'location', 'attendees', 'voting_options', 'start_date', 'end_date')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

class VotingOptionForm(forms.ModelForm):

    class Meta:
        model = VotingOption
        fields = ('title', 'category', 'description', 'image')
        widgets = {
            'image': FileInput(),
        }