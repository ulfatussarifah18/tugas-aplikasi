# Generated by Django 5.0.4 on 2024-05-17 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0001_initial'),
        ('pinjaman', '0002_rename_jumlah_simpanan_pinjaman_jangka_waktu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjaman',
            name='nama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pinjaman', to='anggota.anggota'),
        ),
    ]
