from django.shortcuts import render, get_object_or_404, redirect
from .models import Pessoa
from .forms import PessoaForm

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/listar_pessoas.html', {'pessoas': pessoas})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/cadastrar_pessoa.html', {'form': form})

def consultar_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoas/consultar_pessoa.html', {'pessoa': pessoa})