# serializers.py

from rest_framework import serializers
from .models import Investasi

class InvestasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investasi
        fields = ['nama','deskripsi','jenis','jumlah','tanggal_mulai','tanggal_berakhir']
