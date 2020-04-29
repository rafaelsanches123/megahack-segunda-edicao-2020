from django.db import models

class CadastroModel(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    renda = models.FloatField()
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.cad_usuario