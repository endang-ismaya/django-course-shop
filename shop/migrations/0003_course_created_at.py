# Generated by Django 5.1.6 on 2025-03-01 09:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_category_course_category_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
