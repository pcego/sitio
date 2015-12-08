# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_auto_20151207_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='foto',
        ),
        migrations.AddField(
            model_name='foto',
            name='album',
            field=models.ForeignKey(to='sitio.Album', null=True),
        ),
    ]
