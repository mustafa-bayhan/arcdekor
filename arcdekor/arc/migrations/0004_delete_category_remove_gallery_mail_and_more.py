# Generated by Django 4.1 on 2022-09-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arc', '0003_category_gallery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='mesaj',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='telefon',
        ),
        migrations.AddField(
            model_name='gallery',
            name='kategori',
            field=models.CharField(choices=[('Banyo', 'Banyo'), ('Salon', 'Mutfak'), ('Banyo', 'Banyo'), ('Koridor', 'Koridor'), ('Ofis', 'Ofis')], max_length=50, null=True),
        ),
    ]