from django.db import models
from django.contrib.postgres.fields import JSONField

class GastosModel(models.Model):
    
    class Meta:
        db_table = 'gastos'
    
    nome = models.CharField(max_length=100, primary_key=True)
    valor = models.FloatField()
    data = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome