from django.urls import path 
from Investasi import views

urlpatterns = [
    path('Investasi/', views.InvestasiList.as_view()),
]