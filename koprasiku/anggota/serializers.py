from rest_framework import serializers
from .models import Anggota

class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = ['id', 'nama', 'email', 'nomor_hp', 'tanggal_lahir', 'tanggal_bergabung']
