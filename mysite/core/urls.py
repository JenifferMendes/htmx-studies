from django.urls import path
from .views import home, lista_produtos, cria_produto


urlpatterns = [
    path('', home, name='home'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('produtos/novo/', cria_produto, name='cria_produto'),
]
