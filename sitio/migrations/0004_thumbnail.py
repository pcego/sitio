# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_auto_20151205_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='/thumbnails')),
                ('album', models.ForeignKey(to='sitio.Album')),
            ],
        ),
    ]
