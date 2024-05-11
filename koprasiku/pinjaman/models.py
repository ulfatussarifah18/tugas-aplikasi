from django.db import models

class pinjaman(models.Model):
    nama= models.CharField(max_length=100)
    nomor_hp = models.CharField(max_length=15, unique=True)
    jumlah_pinjaman= models.CharField(max_length=100)
    jangka_waktu= models.DateField()
    tanggal_pinjaman= models.DateField(auto_now_add=True)
    status_pinjaman= models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama
