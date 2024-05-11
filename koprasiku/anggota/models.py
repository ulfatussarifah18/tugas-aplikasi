from django.db import models

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    nomor_hp = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    tanggal_lahir = models.DateField()
    tanggal_bergabung = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nama