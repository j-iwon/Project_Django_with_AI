# Generated by Django 5.0.2 on 2024-03-12 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='wishlistreply',
            options={'ordering': ['-id']},
        ),
    ]
