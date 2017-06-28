# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-26 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairwise_comparisons', '0003_auto_20170626_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='media/csv_files')),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_file',
            field=models.FileField(upload_to='media/ordinary_files'),
        ),
    ]
