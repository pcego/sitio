# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='album',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='foto',
            field=models.ForeignKey(null=True, to='sitio.Foto'),
        ),
        migrations.AddField(
            model_name='album',
            name='thumbnail',
            field=models.ForeignKey(null=True, to='sitio.Thumbnail'),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/'),
        ),
    ]
