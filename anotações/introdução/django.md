# 🧠 O que é Django

Django é um **framework web** em Python que permite criar sites e APIs rapidamente.
Ele segue o padrão **MVT (Model–View–Template)**, parecido com o **MVC** usado em outras linguagens.

### 📦 Estrutura básica MVT
O MVT é o coração da arquitetura do Django.
Ele separa sua aplicação em 3 partes principais, cada uma com uma responsabilidade bem definida:
| Parte        | Significado            | Responsabilidade principal                                     | Exemplo  |
| ------------ | ---------------------- | -------------------------------------------------------------- | -----|
| **Model**    | Representa os dados    | Define o formato das informações que vão para o banco de dados  | `class Produto(models.Model)` |
| **View**     | Lida com a lógica      | Controla o que acontece quando o usuário acessa uma página    | `def home(request): return render(...)` |
| **Template** | Representa a interface | Define o que o usuário vê na tela (HTML)                      | `home.html` |


## ⚙️ Instalação e primeiro projeto

1. **Crie um ambiente virtual**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

2. **Instale o Django**

   ```bash
   pip install django
   ```

3. **Crie um projeto**

   ```bash
   django-admin startproject mysite
   cd mysite
   ```

   Estrutura criada:

   ```
   mysite/
   ├── manage.py
   ├── mysite/
       ├── __init__.py
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
   ```

4. **Rode o servidor**

   ```bash
   python manage.py runserver
   ```

   ➜ Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   Você verá a tela “It worked!” do Django.

---

## 🧭 O que é cada arquivo

* **manage.py** → comando principal (rodar servidor, criar apps, migrar banco etc.)
* **settings.py** → configurações do projeto.
* **urls.py** → define as rotas.
* **wsgi.py** → interface entre o Django e o servidor web.

---

## 📘 Conceito importante: App

Um *app* é um módulo dentro do projeto (como “produtos”, “clientes”, “blog” etc.).
Um projeto pode ter vários apps.

Criar app:

```bash
python manage.py startapp core
```

Nova pasta:

```
core/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
```
---

Abra mysite/settings.py e adicione core:
```python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ← adicione isto
]
```


#  Criando sua Primeira Página no Django**

> **URL → View → Template**

---

## 🚩 Passo 1: Criar sua primeira *view*

Abra o arquivo `core/views.py` e substitua o conteúdo por:

```python
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Olá, Django está funcionando!")
```

> 🧠 Essa *view* recebe a requisição (request) e devolve uma resposta simples (response).
> Mais tarde trocaremos o `HttpResponse` por um **template HTML**.

---

## 🧭 Passo 2: Criar a rota (URL)

Abra o arquivo principal de rotas:
`mysite/urls.py`

Adicione o caminho para sua nova view:

```python
from django.contrib import admin
from django.urls import path
from core.views import home  # importa a view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # rota raiz do site
]
```

> Agora, acessar `http://127.0.0.1:8000/` chamará a função `home()` do seu app.




Teste com:

```bash
python manage.py runserver
```

➡️ Vá no navegador → **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
Deve aparecer:
**“Olá, Django está funcionando!”**

---

## 🧱 Passo 3: Usar um *template* (HTML)

Agora vamos substituir o texto fixo por uma página HTML.

1. Dentro da pasta `core/`, crie uma pasta chamada **templates**
   e dentro dela um arquivo chamado **home.html**:

```
core/
 ├── templates/
 │     └── home.html
 ├── views.py
 ├── models.py
 ...
```

2. Escreva um HTML simples:

```html
<!-- core/templates/home.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Minha primeira página Django</title>
</head>
<body>
    <h1>Bem-vindo ao meu primeiro site Django!</h1>
    <p>Essa página foi renderizada usando o sistema de templates do Django 😎</p>
</body>
</html>
```

3. Atualize a view para usar o template:

```python
# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

> A função `render()` procura o arquivo `home.html` na pasta `templates/` e o mostra no navegador.

---

## 🧩 Estrutura final até agora

```
mysite/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
├── core/
│   ├── views.py
│   ├── templates/
│   │   └── home.html
```

---

01/11/2025


#  Criar o Model

`core/models.py`

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} (R$ {self.preco})"
```

> Dica: `__str__` deixa a listagem mais legível no Admin e no shell.

---

# Migrar o banco

No terminal (na pasta do projeto, onde está o `manage.py`):

```bash
python manage.py makemigrations
python manage.py migrate
```

Isso cria a tabela `core_produto` no SQLite padrão (`db.sqlite3`).

---

# Registrar no Django Admin

`core/admin.py`

```python
from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque", "criado_em")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("criado_em",)
    ordering = ("-criado_em",)
```

Crie um superusuário e acesse o painel:

```bash
python manage.py createsuperuser
python manage.py runserver
# entrar em: http://127.0.0.1:8000/admin
```

Cadastre alguns **Produtos** pelo Admin.


---

# Exibir dados no Template

### View

`core/views.py`

```python
from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.order_by("-criado_em")  # mais recentes primeiro
    return render(request, "produtos.html", {"produtos": produtos})
```

### URL

`mysite/urls.py`

```python
from django.contrib import admin
from django.urls import path
from core.views import home, lista_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('produtos/', lista_produtos),
]
```

### Template

`core/templates/produtos.html`

```html
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>Produtos</title>
</head>
<body>
  <h1>Produtos</h1>

  {% if produtos %}
    <ul>
      {% for p in produtos %}
        <li>
          <strong>{{ p.nome }}</strong> — R$ {{ p.preco }} 
          (Estoque: {{ p.estoque }})
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p>Nenhum produto cadastrado ainda.</p>
  {% endif %}

  <p><a href="/admin/">Abrir Admin</a></p>
</body>
</html>
```
va em mysite/urls e coloque:

```python
from core.views import home, lista_produtos 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # rota raiz do site
    path('produtos/', lista_produtos),
]
```

Abra: `http://127.0.0.1:8000/produtos/` — você verá os itens que cadastrou.

---
(não fiz essa parte, mas se precisar)

# Popular via shell

Se preferir criar dados rápido:

```bash
python manage.py shell
```

```python
from core.models import Produto
Produto.objects.create(nome="Teclado", preco=199.90, estoque=12)
Produto.objects.create(nome="Mouse", preco=89.50, estoque=30)
Produto.objects.create(nome="Monitor", preco=1299.00, estoque=7)
exit()
```

Recarregue `/produtos/`.

---

