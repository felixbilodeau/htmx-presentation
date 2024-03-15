# Generated by Django 4.2.11 on 2024-03-14 23:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('content', models.CharField(max_length=255, verbose_name='Content')),
                ('edited', models.BooleanField(default=False, verbose_name='Edited')),
            ],
        ),
    ]
