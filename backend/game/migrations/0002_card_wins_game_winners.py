# Generated by Django 5.0.3 on 2025-01-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='wins',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='game',
            name='winners',
            field=models.JSONField(default=dict),
        ),
    ]
