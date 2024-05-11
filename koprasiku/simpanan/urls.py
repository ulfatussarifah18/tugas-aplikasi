from django.urls import path 
from simpanan import views

urlpatterns = [
    path('simpanan/', views.simpananList.as_view()),
]
