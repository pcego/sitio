# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='album',
            field=models.ForeignKey(to='sitio.Album', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foto',
            name='legenda',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='album',
            name='nome',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(upload_to='./static/media/'),
        ),
    ]
