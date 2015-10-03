import re
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from filer.fields.image import FilerImageField

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class VotingOption(models.Model):

  CATEGORY_CHOICES = (
      ('Budget', 'Budget'),
      ('Date', 'Date'),
      ('Meal','Meal'),
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

class Event(models.Model):
  organizer = models.ForeignKey(User)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  location = models.CharField(max_length=100)
  # TO DO: make users
  attendees = models.TextField()
  attendees_text_field = models.TextField()
  voting_options = models.ManyToManyField(VotingOption)
  start_date = models.DateField()
  end_date = models.DateField()
  slug = models.SlugField(null=True, blank=True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    attendee_list = re.findall(r'[^,;\s]+', self.attendees_text_field)
    self.attendees.extend(attendee_list)
    super(Event, self).save(*args, **kwargs)

  # on save - send email/texts
  def __unicode__(self):
    return self.title
