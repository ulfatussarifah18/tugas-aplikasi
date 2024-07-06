# Generated by Django 5.0.4 on 2024-05-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0002_alter_anggota_options_alter_anggota_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anggota',
            options={},
        ),
        migrations.AlterField(
            model_name='anggota',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='nomor_hp',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='tanggal_lahir',
            field=models.DateField(),
        ),
    ]