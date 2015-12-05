# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_auto_20151125_2345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name_plural': 'albuns'},
        ),
        migrations.AlterModelOptions(
            name='foto',
            options={'verbose_name': 'Foto'},
        ),
        migrations.RemoveField(
            model_name='foto',
            name='legenda',
        ),
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
    ]
