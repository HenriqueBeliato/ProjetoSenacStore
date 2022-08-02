from turtle import width
from django.contrib import admin
from django.utils.html import mark_safe

from Store.models import Categoria, Departamento, Produto

# Register your models here.

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'departamento']
    list_display_links = ['id', 'nome']
    list_filter = ['departamento']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'estoque', 'categoria', 'ver_imagem']
    list_display_links = ['id', 'nome']
    list_filter = ['categoria']
    search_fields = ['nome']
    readonly_fields = ['ver_imagem']

    def ver_imagem(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.imagem.url,
            width=75,
            height=75,
        )
    )


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)