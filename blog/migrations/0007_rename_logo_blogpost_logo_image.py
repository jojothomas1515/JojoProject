# Generated by Django 4.0.4 on 2022-06-11 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_author_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='BlogPost',
            old_name='logo',
            new_name='logo_image',
        ),
    ]
