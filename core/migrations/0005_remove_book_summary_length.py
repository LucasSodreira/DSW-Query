# Generated by Django 5.0 on 2023-12-09 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_book_summary_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='summary_length',
        ),
    ]
