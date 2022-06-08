# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('duratin', models.IntegerField()),
            ],
        ),
    ]
