from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.messages import constants as message_constants
from .forms import LoginForm, RegistroForm, ContatoModelForm

from .models import Funcionarios, Produto, Cliente



# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def produtos(request):
    # Busca todos os produtos cadastrados
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request,'produtos.html', context)

@login_required
def clientes(request):
    # Busca todos os clientes cadastrados
    clientes = Cliente.objects.all().order_by('nome_completo')
    context = {
        'clientes': clientes
    }
    return render(request,'clientes.html', context)

# FUNÇÃO CORRIGIDA/RESTAURADA
@login_required
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

# A view principal do formulário
@login_required
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
@login_required
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')



#login

# View protegida que requer autenticação para acesso.
@login_required
def home(request):
    # Obtém o número de visitas armazenado na sessão, incrementa em 1 e atualiza na sessão.
    visitas = request.session.get('visitas', 0) + 1
    request.session['visitas'] = visitas

    # Renderiza o template 'home.html' passando o número de visitas como contexto.
    return render(request, 'home.html', {'visitas': visitas })

# View para realizar login.
def login_view(request):
    # Se o usuário já estiver autenticado, redireciona para a página inicial.
    if request.user.is_authenticated:
        return redirect('home')

    # Cria uma instância do formulário de login com os dados enviados (se houver).
    form = LoginForm(request.POST or None)

    # Verifica se o método da requisição é POST e se o formulário é válido.
    if request.method == 'POST' and form.is_valid():
        # Autentica o usuário com base nos dados do formulário.
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        # Se a autenticação for bem-sucedida, realiza o login e redireciona para a página inicial.
        if user:
            login(request, user) # Cria e atualiza a sessão do usuário.
            messages.success(request, 'Login Realizado')
            return redirect('home')

        # Caso contrário, exibe uma mensagem de erro.
        messages.error(request, 'Credenciais inválidas')

    # Renderiza o template 'login.html' passando o formulário como contexto.
    return render(request, 'login.html', {'form': form })

# View para registrar um novo usuário.
def registrar_view(request):
    # Se o usuário já estiver autenticado, redireciona para a página inicial.
    if request.user.is_authenticated:
        return redirect('home')

    # Cria uma instância do formulário de registro com os dados enviados (se houver).
    form = RegistroForm(request.POST or None)

    # Verifica se o método da requisição é POST e se o formulário é válido.
    if request.method == 'POST' and form.is_valid():
        # Cria um novo usuário com base nos dados do formulário.
        user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email= form.cleaned_data['email'],
            password= form.cleaned_data['password'],
        )

        # Exibe uma mensagem de sucesso e redireciona para a página de login.
        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')

    # Renderiza o template 'registrar.html' passando o formulário como contexto.
    return render(request, 'registrar.html', {'form': form})

# View protegida que requer autenticação para acesso ao perfil do usuário.
@login_required
def perfil(request):
    # Renderiza o template 'perfil.html'.
    return render(request, 'perfil.html')

# View para realizar logout.
def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão.
    logout(request)

    # Exibe uma mensagem informativa e redireciona para a página de login.
    messages.info(request, 'Você saiu')
    return redirect('login')    
