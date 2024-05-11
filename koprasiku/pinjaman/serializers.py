from rest_framework import serializers
from .models import pinjaman

class pinjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pinjaman 
        fields = ['nama', 'nomor_hp','jumlah_pinjaman', 'jangka_waktu', 'tanggal_pinjaman','status_pinjaman']
