# Generated by Django 2.1.7 on 2019-04-10 03:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0002_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='id',
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]