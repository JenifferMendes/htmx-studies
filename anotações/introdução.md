assistindo o curso: https://www.youtube.com/watch?v=Yr-ubS0H7z4&list=PL4cUxeGkcC9gnEsXRqdY4e_xNy9GK7aQR


# O que é HTMX?
É uma biblioteca do javascript que nos permite fazer aplicativos web dinâmicos
Using a hypermedia Approach.

Hypermedia Controls
<a href="/some/path">click</a>

O htmx é uma biblioteca JavaScript leve que permite adicionar interatividade em páginas web de forma simples, sem precisar escrever tanto código em JavaScript.



A ideia principal do htmx é estender o HTML com atributos que permitem:



Fazer requisições HTTP (GET, POST, PUT, DELETE) diretamente a partir de elementos HTML.



Substituir ou atualizar partes da página com o resultado da requisição (sem precisar recarregar tudo).



Criar interações dinâmicas (como abas, filtros, formulários dinâmicos, rolagem infinita) usando apenas atributos HTML.



# Benefícios do htmx



Menos JavaScript: você escreve a lógica de interação declarativamente em atributos HTML.



Progressive enhancement: se o htmx não funcionar, a página ainda é utilizável.



Integração com back-end: facilita usar frameworks que já renderizam HTML no servidor (Django, Flask, Rails, Spring, etc.).



Mais simples que SPA tradicionais: não precisa de React, Vue ou Angular para muitos casos.



Devo saber sobre HTML para começar.
Saber sobre metodos de request.


# RESQUEST METHODS

Request methods (ou métodos de requisição HTTP) são formas diferentes de um navegador (ou qualquer cliente) falar com um servidor usando o protocolo HTTP.
Eles indicam qual ação você quer que o servidor faça.

## Principais métodos HTTP

## GET

Usado para pedir dados ao servidor.


Exemplo: quando você entra em https://meusite.com/produtos, o navegador faz um GET /produtos.


Não deve modificar nada no servidor, só buscar informação.

## POST

Usado para enviar dados ao servidor (geralmente criar algo novo).


Exemplo: enviar um formulário de cadastro (POST /usuarios).


## PUT

Usado para atualizar um recurso existente no servidor.


Exemplo: editar um usuário (PUT /usuarios/5).


## PATCH

Parecido com PUT, mas atualiza parcialmente um recurso.


Exemplo: mudar só o email de um usuário.


## DELETE

Usado para apagar um recurso.


Exemplo: deletar um usuário (DELETE /usuarios/5).


## HEAD

Igual ao GET, mas só traz os headers (sem o corpo da resposta).

Útil para verificar se um recurso existe ou checar metadados.

## OPTIONS

Pergunta ao servidor quais métodos são permitidos para um recurso.

Usado em cenários de CORS, por exemplo.

**Exemplo prático (REST API)**

Se você tem um recurso usuarios em uma API, poderia interagir assim:

- GET /usuarios → lista todos os usuários

- GET /usuarios/10 → pega o usuário com ID 10

- POST /usuarios → cria um novo usuário

- PUT /usuarios/10 → atualiza totalmente o usuário 10

- PATCH /usuarios/10 → atualiza parcialmente o usuário 10

- DELETE /usuarios/10 → apaga o usuário 10

Resumindo: request methods são os verbos do HTTP — eles dizem o que você quer fazer com um recurso no servidor.

## API Conceito


O que é uma API?

API significa Application Programming Interface (Interface de Programação de Aplicações). Ou seja,
Uma API é um conjunto de regras e ferramentas que permite que um software se comunique com outro.

Você pode pensar nela como um garçom em um restaurante:

- Você (cliente) pede um prato (requisição).

- O garçom (API) leva o pedido até a cozinha (servidor).

- A cozinha prepara o prato e devolve ao garçom.

-O garçom traz o prato pronto para você (resposta).

## Tipos mais comuns

APIs Web (REST, GraphQL, etc.) → permitem que aplicações conversem pela internet.

APIs de bibliotecas/softwares → funções prontas que você pode usar em código.

API é como uma ponte — você pede algo para um sistema, ele processa e devolve o resultado em um formato que sua aplicação entende.

-> baixar nodejs