from django.db import models

class pinjaman(models.Model):
    nama= models.CharField(max_length=100)
    nomor_hp = models.CharField(max_length=15, unique=True)
    jenis_simpanan= models.CharField(max_length=100)
    jumlah_simpanan= models.DateField()
    tanggal_simpanan= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nama
