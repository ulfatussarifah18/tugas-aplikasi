from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include ('anggota.urls')),
    path('', include ('pinjaman.urls')),
    path('', include('simpanan.urls')),
    path('', include('Investasi.urls')),
]
