# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_attendees_text_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.TextField(default=datetime.datetime(2015, 10, 3, 23, 34, 16, 495363, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
