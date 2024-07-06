from rest_framework import serializers
from .models import Pinjaman

class PinjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pinjaman 
        fields = ['nama', 'nomor_hp','jumlah_pinjaman', 'jangka_waktu', 'tanggal_pinjaman','status_pinjaman']
