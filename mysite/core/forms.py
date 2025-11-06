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
