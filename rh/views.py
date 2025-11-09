from django.shortcuts import redirect, render
# Certifique-se de importar todos os modelos: Funcionarios, Produto e Cliente
from .models import Funcionarios, Produto, Cliente 
from .forms import ContatoModelForm

# Create your views here.
def home(request):
    return render(request,'home.html')

# NOVO: View de Produtos
def produtos(request):
    # Busca todos os produtos cadastrados
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request,'produtos.html', context)

# NOVO: View de Clientes
def clientes(request):
    # Busca todos os clientes cadastrados
    clientes = Cliente.objects.all().order_by('nome_completo')
    context = {
        'clientes': clientes
    }
    return render(request,'clientes.html', context)

# View de Funcionários (Deve estar com o nome correto: funcionarios, em minúsculas)
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

# A view principal do formulário
def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    
    else:
        form = ContatoModelForm()

    return render(request, 'contato/contatos.html', {'form': form})


# Uma view simples para a página de "sucesso"
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')