# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendees_text_field',
        ),
    ]
