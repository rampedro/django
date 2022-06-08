# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(related_name='arrivals', to='flight.Airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(related_name='departures', to='flight.Airport'),
        ),
    ]
