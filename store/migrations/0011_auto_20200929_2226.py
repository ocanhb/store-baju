# Generated by Django 3.1.1 on 2020-09-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='porduct',
            new_name='product',
        ),
    ]
