from django.db import models
from anggota.models import Anggota

class Investasi(models.Model):
    nama= models.ForeignKey(Anggota, on_delete=models.CASCADE)
    deskripsi = models.TextField()
    jenis = models.CharField(max_length=50)
    jumlah = models.DecimalField(max_digits=15, decimal_places=2)
    tanggal_mulai = models.DateField()
    tanggal_berakhir = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nama