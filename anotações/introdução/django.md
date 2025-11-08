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

# Crie o `forms.py` (ModelForm + validação)

`core/forms.py`

```python
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco", "estoque"]

    # Exemplo simples de validação
    def clean_preco(self):
        preco = self.cleaned_data["preco"]
        if preco <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return preco
```

---

# Views: listar e criar (GET/POST + mensagens)

`core/views.py`

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

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
```

> Notas
> • `messages.success` / `messages.error` aparecem no template (vamos montar já).
> • `redirect("lista_produtos")` usa **nome de rota** (vamos nomear na URL).

---

# 3) URLs: inclua rota “novo produto”

Se você está usando **`mysite/urls.py`** diretamente:

```python
from django.contrib import admin
from django.urls import path
from core.views import home, lista_produtos, cria_produto

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("produtos/", lista_produtos, name="lista_produtos"),
    path("produtos/novo/", cria_produto, name="cria_produto"),
]
```

Ou, se usa **`core/urls.py`** + `include`:

```python
# core/urls.py
from django.urls import path
from .views import home, lista_produtos, cria_produto

urlpatterns = [
    path("", home, name="home"),
    path("produtos/", lista_produtos, name="lista_produtos"),
    path("produtos/novo/", cria_produto, name="cria_produto"),
]
```

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
```

---

# 4) Herança de templates (boilerplate + mensagens)

## `core/templates/base.html`

```html
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8">
  <title>{% block title %}Meu Site{% endblock %}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 24px; }
    nav a { margin-right: 12px; }
    .messages { margin: 12px 0; padding: 0; list-style: none; }
    .messages li { padding: 10px 12px; border-radius: 8px; margin-bottom: 8px; }
    .messages li.success { background: #e7f6ec; border: 1px solid #b7e2c1; }
    .messages li.error   { background: #fde8e8; border: 1px solid #f5c2c7; }
  </style>
</head>
<body>
  <nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'lista_produtos' %}">Produtos</a>
    <a href="{% url 'cria_produto' %}">Novo produto</a>
  </nav>

  {% if messages %}
    <ul class="messages">
      {% for message in messages %}
        <li class="{{ message.tags }}">{{ message }}</li>
      {% endfor %}
    </ul>
  {% endif %}

  {% block content %}{% endblock %}
</body>
</html>
```

> O Django já vem com o **messages framework** habilitado para templates; no seu `settings.py` ele já traz os context processors necessários (como vimos no dump).

---

# 5) Atualize os templates para herdar de `base.html`

## `core/templates/produtos.html`

```html
{% extends "base.html" %}
{% block title %}Produtos{% endblock %}
{% block content %}
  <h1>Produtos</h1>

  {% if produtos %}
    <ul>
      {% for p in produtos %}
        <li>
          <strong>{{ p.nome }}</strong> — R$ {{ p.preco }} (Estoque: {{ p.estoque }})
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p>Nenhum produto cadastrado ainda.</p>
  {% endif %}
{% endblock %}
```

## `core/templates/produto_form.html`

```html
{% extends "base.html" %}
{% block title %}Novo produto{% endblock %}
{% block content %}
  <h1>Novo produto</h1>

  <form method="post" novalidate>
    {% csrf_token %}
    {{ form.non_field_errors }}

    <p>
      {{ form.nome.label_tag }}<br>
      {{ form.nome }}
      {% for error in form.nome.errors %}<small style="color:#b00">{{ error }}</small>{% endfor %}
    </p>

    <p>
      {{ form.preco.label_tag }}<br>
      {{ form.preco }}
      {% for error in form.preco.errors %}<small style="color:#b00">{{ error }}</small>{% endfor %}
    </p>

    <p>
      {{ form.estoque.label_tag }}<br>
      {{ form.estoque }}
      {% for error in form.estoque.errors %}<small style="color:#b00">{{ error }}</small>{% endfor %}
    </p>

    <button type="submit">Salvar</button>
  </form>
{% endblock %}
```

> Quer simplificar? troque os campos por `{{ form.as_p }}`.
> Quer deixar mais bonito? depois podemos plugar Bootstrap (sem mudar a lógica).

---

# Teste rápido

1. Acesse **/produtos/** (lista vazia).
2. Vá em **/produtos/novo/**, preencha e salve.
3. Você deve ser redirecionado para a lista, com **mensagem de sucesso** no topo.

---
vai **no `forms.py`**, dentro da sua classe `ProdutoForm`.
Segue o arquivo completo para você **copiar e colar**:

`core/forms.py`

```python
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "preco", "estoque"]

        # <- AQUI entram os placeholders e outros atributos de HTML
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Ex.: Teclado mecânico",
                "autofocus": "autofocus"
            }),
            "preco": forms.NumberInput(attrs={
                "step": "0.01",   # passo de centavos
                "min": "0"        # não deixa digitar negativo
            }),
            "estoque": forms.NumberInput(attrs={
                "min": "0"
            }),
        }

        # (opcional) rótulos bonitinhos
        labels = {
            "nome": "Nome do produto",
            "preco": "Preço (R$)",
            "estoque": "Estoque",
        }

    # (opcional) validação extra
    def clean_preco(self):
        preco = self.cleaned_data["preco"]
        if preco <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return preco
```


perfeito — vamos **finalizar o teste** e seguir pro **CRUD completo**.

# ✅ Teste rápido (garantia de que está tudo OK)

1. Abra **/produtos/**
   – Se não houver itens, deve mostrar “Nenhum produto cadastrado ainda.”

2. Vá em **/produtos/novo/**, preencha e **Salvar**
   – Se tudo certo, você será **redirecionado para /produtos/** com a **mensagem verde** no topo:
   `Produto "<nome>" criado com sucesso!`

3. Se algo **não aparecer**:

   * `base.html` precisa ter o bloco das mensagens (aquele `<ul class="messages">…`).
   * A view `cria_produto` precisa ter `messages.success(...)` e `redirect("lista_produtos")`.
   * A URL `lista_produtos` deve existir com `name="lista_produtos"`.

Tudo certinho? Então bora para **editar e excluir**.

---

# Editar e Excluir (Update/Delete)

## Views

`core/views.py`

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

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
```

## 2) URLs

Se você está usando **mysite/urls.py** direto:

```python
from django.contrib import admin
from django.urls import path
from core.views import home, lista_produtos, cria_produto, edita_produto, exclui_produto

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("produtos/", lista_produtos, name="lista_produtos"),
    path("produtos/novo/", cria_produto, name="cria_produto"),
    path("produtos/<int:pk>/editar/", edita_produto, name="edita_produto"),
    path("produtos/<int:pk>/excluir/", exclui_produto, name="exclui_produto"),
]
```

(Se usa `core/urls.py`, copie essas linhas para lá e mantenha o `include` no `mysite/urls.py`.)

## 3) Templates

### 3.1. Reaproveite `produto_form.html`

Ele já serve para **criar** e **editar**. Só adicione um título condicional:

```django
{% extends "base.html" %}
{% block title %}{{ produto|default_if_none:"Novo" }} produto{% endblock %}
{% block content %}
  <h1>{{ produto|default_if_none:"Novo" }} produto</h1>
  <form method="post" novalidate>
    {% csrf_token %}
    {{ form.non_field_errors }}
    <p>{{ form.nome.label_tag }}<br>{{ form.nome }}{% for e in form.nome.errors %}<small style="color:#b00">{{ e }}</small>{% endfor %}</p>
    <p>{{ form.preco.label_tag }}<br>{{ form.preco }}{% for e in form.preco.errors %}<small style="color:#b00">{{ e }}</small>{% endfor %}</p>
    <p>{{ form.estoque.label_tag }}<br>{{ form.estoque }}{% for e in form.estoque.errors %}<small style="color:#b00">{{ e }}</small>{% endfor %}</p>
    <button type="submit">Salvar</button>
  </form>
{% endblock %}
```

### 3.2. Confirmação de exclusão

`core/templates/produto_confirm_delete.html`

```django
{% extends "base.html" %}
{% block title %}Excluir produto{% endblock %}
{% block content %}
  <h1>Excluir produto</h1>
  <p>Tem certeza que deseja excluir <strong>{{ produto.nome }}</strong>?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Sim, excluir</button>
    <a href="{% url 'lista_produtos' %}">Cancelar</a>
  </form>
{% endblock %}
```

### 3.3. Links na lista

`core/templates/produtos.html`

```django
{% extends "base.html" %}
{% block title %}Produtos{% endblock %}
{% block content %}
  <h1>Produtos</h1>
  {% if produtos %}
    <ul>
      {% for p in produtos %}
        <li>
          <strong>{{ p.nome }}</strong> — R$ {{ p.preco }} (Estoque: {{ p.estoque }})
          · <a href="{% url 'edita_produto' p.pk %}">Editar</a>
          · <a href="{% url 'exclui_produto' p.pk %}">Excluir</a>
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p>Nenhum produto cadastrado ainda.</p>
  {% endif %}
{% endblock %}
```

## 4) Teste

1. Crie 1–2 produtos em **/produtos/novo/**.
2. Clique **Editar** → altere preço → **Salvar** (volta para a lista com mensagem).
3. Clique **Excluir** → confirme → volta com mensagem.

Se algo quebrar, me diga a mensagem (linha/arquivo) e eu ajusto.
Quer que na sequência eu adicione **busca e paginação** na lista, ou preferir **Bootstrap** para deixar a UI mais bonitinha?
