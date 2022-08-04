from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from Store.models import Departamento
from Store.models import Categoria
from Store.models import Produto


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



def departamentos(request):
    dpto = Departamento.objects.all()
    context = {'departamentos': dpto}
    return render(request, 'departamentos.html', context)



def lista_categ(request):
    lista_categorias = Categoria.objects.all()
    context = {'categorias': lista_categorias}
    return render(request, 'categorias.html', context)



def categorias(request, id):
    lista_categorias = Categoria.objects.filter(departamento_id = id)
    depto = Departamento.objects.get(id = id)
    context = {
        'categorias': lista_categorias,
        'departamento': depto
        }
    return render(request, 'categorias.html', context) 



def lista_prod(request):
    relacao_produtos = Produto.objects.all()
    context = {'categorias': relacao_produtos}
    return render(request, 'Produtos.html', context)



def produtos(request, id):
    relacao_produtos = Produto.objects.filter(categoria_id = id)
    prod = Categoria.objects.get(id = id)
    context = {
        'Produtos': relacao_produtos,
        'Categoria': prod
        }
    return render(request, 'Produtos.html', context)



def produto_detalhe(request, id):
    det_prod = Produto.objects.get(id = id)
    context = {
        'Produto_Detalhe': det_prod,
        'Produto': det_prod
        }
    return render(request, 'produto_detalhe.html', context)
