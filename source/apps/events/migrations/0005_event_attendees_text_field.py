# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees_text_field',
            field=models.TextField(default=datetime.datetime(2015, 10, 3, 21, 30, 58, 659228, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
