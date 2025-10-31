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
