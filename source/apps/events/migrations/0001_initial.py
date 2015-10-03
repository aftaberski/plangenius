# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VotingOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(default=b'Activity', max_length=200, choices=[(b'Budget', b'Budget'), (b'Date', b'Date'), (b'Meal', b'Meal'), (b'Accommodation', b'Accommodation'), (b'Activity', b'Activity')])),
                ('description', models.TextField(max_length=255)),
                ('score', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
