from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Produto
from django.contrib import messages
from .forms import ProdutoForm


def home(request):
    return render(request, 'home.html')


def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")
    return render(request, "produtos.html", {"produtos": produtos})


def cria_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f'Produto "{produto.nome}" criado com sucesso!')
            return redirect("lista_produtos")
        else:
            messages.error(request, "Corrija os erros abaixo e tente novamente.")
    else:
        form = ProdutoForm()
    return render(request, "produto_form.html", {"form": form})
