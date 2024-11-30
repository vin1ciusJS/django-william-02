from django.db import models
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario

class NotaFiscal(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Nota {self.id} - {self.cliente.nome}'