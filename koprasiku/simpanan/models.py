from django.db import models
from anggota.models import Anggota


class simpanan(models.Model):
    nama= models.ForeignKey(Anggota, related_name='simpanan', on_delete=models.CASCADE)
    nomor_hp = models.CharField(max_length=15, unique=True)
    jenis_simpanan= models.CharField(max_length=100)
    jumlah_simpanan= models.DateField()
    tanggal_simpanan= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nama

