# Generated by Django 4.0.4 on 2022-05-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_summary_alter_blogpost_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='head image'),
        ),
    ]