from django.db import models


class CadastroModel(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    senha = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    renda = models.FloatField()
    gasto = models.FloatField()

    def __str__(self):
        return self.email
