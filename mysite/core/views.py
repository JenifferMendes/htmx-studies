from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto


def home(request):
    return render(request, 'home.html')


def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")
    return render(request, "produtos.html", {"produtos": produtos})
