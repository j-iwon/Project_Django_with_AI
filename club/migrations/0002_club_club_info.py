# Generated by Django 5.0.2 on 2024-03-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
