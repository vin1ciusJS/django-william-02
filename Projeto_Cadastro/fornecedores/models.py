from django.db import models

class Fornecedor(models.Model):
    nome_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_social