from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from filer.fields.image import FilerImageField

# class Event(models.Model):
#   organizer
#   location
#   attendees
#   voting_options
#   start_date
#   end_date

class VotingOption(models.Model):

  CATEGORY_CHOICES = (
      ('Budget', 'Budget'),
      ('Date', 'Date'),
      ( 'Meal','Meal'),
      ('Accommodation', 'Accommodation'),
      ('Activity', 'Activity'),
  )
  title = models.CharField(max_length=100)
  category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='Activity')
  description = models.TextField(max_length=255)
  score = models.SmallIntegerField(default=0)
  voters = []
  image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='voting_option_image')

  def __unicode__(self):
    return self.title