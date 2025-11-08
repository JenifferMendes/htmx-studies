from django.shortcuts import render, redirect, get_object_or_404
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
        messages.error(request, "Corrija os erros abaixo e tente novamente.")
    else:
        form = ProdutoForm()
    return render(request, "produto_form.html", {"form": form, "produto": None})


def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produto "{produto.nome}" atualizado!')
            return redirect("lista_produtos")
        messages.error(request, "Corrija os erros e tente novamente.")
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "produto_form.html", {"form": form, "produto": produto})


def exclui_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        nome = produto.nome
        produto.delete()
        messages.success(request, f'Produto "{nome}" excluído!')
        return redirect("lista_produtos")
    return render(request, "produto_confirm_delete.html", {"produto": produto})

