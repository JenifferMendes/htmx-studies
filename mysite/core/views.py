from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.contrib import messages
from .forms import ProdutoForm
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')



def lista_produtos(request):
    # 1) Busca
    termo = request.GET.get("q", "").strip()

    produtos = Produto.objects.all()

    if termo:
        produtos = produtos.filter(nome__icontains=termo)

    # 2) Filtros
    filtro_estoque = request.GET.get("estoque", "")
    if filtro_estoque == "sem":
        produtos = produtos.filter(estoque=0)
    elif filtro_estoque == "baixo":
        produtos = produtos.filter(estoque__lte=5)
    elif filtro_estoque == "alto":
        produtos = produtos.filter(estoque__gte=20)

    # 3) Ordenação
    ordenar = request.GET.get("ord", "recente")
    if ordenar == "nome":
        produtos = produtos.order_by("nome")
    elif ordenar == "preco_cresc":
        produtos = produtos.order_by("preco")
    elif ordenar == "preco_desc":
        produtos = produtos.order_by("-preco")
    else:
        produtos = produtos.order_by("-criado_em")  # padrão

    # 4) Paginação
    paginator = Paginator(produtos, 5)  # 5 por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {
        "page_obj": page_obj,
        "termo": termo,
        "filtro_estoque": filtro_estoque,
        "ordenar": ordenar,
    }

    return render(request, "produtos.html", contexto)

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


def produtos_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    produtos = Produto.objects.filter(categoria=categoria).order_by("-criado_em")

    return render(request, "produtos_por_categoria.html", {
        "categoria": categoria,
        "produtos": produtos
    })
