from django.urls import path 
from anggota import views

urlpatterns = [
    path('anggota/', views.Anggota_list),
]

