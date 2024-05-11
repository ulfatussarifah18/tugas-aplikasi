from rest_framework import serializers
from .models import simpanan

class simpananSerializer(serializers.ModelSerializer):
    class Meta:
        model = simpanan
        fields = ['nama', 'nomor_hp','jenis_simpanan', 'jumlah_simpanan', 'tanggal_simpana']
