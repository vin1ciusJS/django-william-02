from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome