# Generated by Django 4.2.10 on 2024-02-07 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('af8d9a2d-393b-47b1-9dc2-6db53f65bf41'), editable=False, primary_key=True, serialize=False),
        ),
    ]
