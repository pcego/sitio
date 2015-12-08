# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_auto_20151206_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='foto',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/', null=True),
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
    ]
