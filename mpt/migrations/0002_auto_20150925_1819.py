# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mpt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
