# Generated by Django 4.0.1 on 2022-01-22 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('scrabble', '0004_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.UUID('75bba261-eb97-4a81-8b54-6e041f9da0cc'), editable=False, primary_key=True, serialize=False),
        ),
    ]
