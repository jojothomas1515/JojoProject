# Generated by Django 4.0.4 on 2022-06-11 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_logo_blogpost_logo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='BlogPost',
            old_name='logo_image',
            new_name='logo',
        ),
    ]