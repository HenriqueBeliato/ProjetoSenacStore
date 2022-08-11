from unicodedata import name
from django.urls import path
from Store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('departamentos/', views.departamentos, name='departamentos'),
    path('categorias/<int:id>', views.categorias, name='categorias'),
    path('produtos/<int:id>', views.produtos, name='produtos'),
    path('produto_detalhe/<int:id>', views.produto_detalhe, name='produto_detalhe'),
    path('institucional/', views.institucional, name='institucional'),
    path('contato/', views.contato, name='contato'),
    path('contato/enviar/', views.enviar_email, name='enviar_contato')
]