# Generated by Django 4.1 on 2022-09-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telefon',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
