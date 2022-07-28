from unicodedata import name
from django.urls import path
from Store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('departamentos/', views.departamentos, name='departamentos'),
    path('categorias/', views.categorias, name='categorias'),
    path('produtos/', views.produtos, name='produtos')
]