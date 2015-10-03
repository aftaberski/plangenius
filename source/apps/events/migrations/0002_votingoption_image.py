# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingoption',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='voting_option_image', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', null=True),
        ),
    ]
