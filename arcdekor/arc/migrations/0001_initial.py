# Generated by Django 4.1 on 2022-09-14 13:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.TextField(null=True)),
                ('mail', models.IntegerField(null=True)),
                ('telefon', models.TextField(null=True)),
                ('mesaj', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
