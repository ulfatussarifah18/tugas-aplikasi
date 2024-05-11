from rest_framework import serializers
from .models import pinjaman

class pinjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = pinjaman 
        fields = ['nama', 'nomor_hp','jenis_simpanan', 'jumlah_simpanan', 'tanggal_simpanan']
