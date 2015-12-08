# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_auto_20151206_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='nome',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
