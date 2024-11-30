from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey('fornecedores.Fornecedor',on_delete=models.CASCADE)

    def __str__(self):
        return self.sobrenome