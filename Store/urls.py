from django.urls import path
from Store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste')
]