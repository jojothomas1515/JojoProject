# Generated by Django 4.0.4 on 2022-05-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Post', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='head image')),
                ('summary', models.CharField(blank=True, max_length=200, null=True)),
                ('pub_date', models.DateField(auto_now=True, verbose_name='Date Published')),
                ('pub_time', models.TimeField(auto_now=True, verbose_name='Time Published')),
            ],
        ),
    ]
