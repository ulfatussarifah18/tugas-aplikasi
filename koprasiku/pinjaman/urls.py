from django.urls import path 
from pinjaman import views

urlpatterns = [
    path('pinjaman/', views.PinjamanList.as_view()),
]
 