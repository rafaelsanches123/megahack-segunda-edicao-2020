from django.db import models
from django.contrib.postgres.fields import JSONField
from project.cadastro.models import CadastroModel

class MetaModel(models.Model):
    
    class Meta:
        db_table = 'meta'
    
    email = models.CharField(max_length=100, primary_key=True)
    descricao = models.TextField()
    valor = models.FloatField()
    data_inicial = models.TextField()
    data_final = models.TextField()
    
    def __str__(self):
        return self.email