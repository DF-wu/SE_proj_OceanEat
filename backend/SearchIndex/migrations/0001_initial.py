# Generated by Django 2.1.7 on 2019-05-16 10:32

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_index', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]