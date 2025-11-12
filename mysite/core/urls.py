from django.contrib import admin
from django.urls import path
from core.views import (
    home, 
    lista_produtos,
    cria_produto,
    edita_produto,
    exclui_produto,
    produtos_por_categoria,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("produtos/", lista_produtos, name="lista_produtos"),
    path("produtos/novo/", cria_produto, name="cria_produto"),
    path("produtos/<int:pk>/editar/", edita_produto, name="edita_produto"),
    path("produtos/<int:pk>/excluir/", exclui_produto, name="exclui_produto"),
    path("categorias/<int:pk>/", produtos_por_categoria, name="produtos_por_categoria"),
]