from django.contrib import admin
from .models import Funcionarios, MensagemContato, Produto, Cliente # Importar novos modelos

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    # Quais colunas mostrar na lista de produtos
    list_display = ('nome', 'cargo', 'departamento', 'data_contratacao','status')
    # Por quais campos podemos buscar
    search_fields = ("nome",)
    # Quais campos podemos filtrar
    list_filter = ('status', 'data_contratacao')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'valor')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'idade', 'email', 'contato')
    search_fields = ('nome_completo', 'email', 'contato')
    list_filter = ('idade',)
    
@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')