from django.urls import path 
from pinjaman import views

urlpatterns = [
    path('pinjaman/', views.pinjamanList.as_view()),
]
