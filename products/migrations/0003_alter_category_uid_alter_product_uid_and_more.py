# Generated by Django 4.2.10 on 2024-02-06 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_uid_alter_product_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('160c3540-8876-4161-a677-b0b38e0c0cb0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('160c3540-8876-4161-a677-b0b38e0c0cb0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('160c3540-8876-4161-a677-b0b38e0c0cb0'), editable=False, primary_key=True, serialize=False),
        ),
    ]