from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento

# Create your views here.
def index(request):
    meu_nome = 'Henrique Beliato da Silva'
    sexo = 'M'
    context = {'nome': meu_nome, 'artigo': 'o' if sexo =='M' else 'a'}
    return render(request, 'index.html', context)

def teste(request):
    # dpto = ['Casa', 'Informática', 'Telefonia', 'Internet', 'Games']
    dpto = Departamento.objects.all()
    context = {'departamentos': dpto}
    return render(request, 'teste.html', context)

