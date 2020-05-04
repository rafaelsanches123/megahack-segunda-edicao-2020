from django.db import models
from django.contrib.postgres.fields import JSONField

class RankingModel(models.Model):
    
    class Meta:
        db_table = 'ranking'
    
    nome_restaurante = models.CharField(max_length=100)
    valor_prato = models.FloatField()
    classificacao = models.IntegerField()
    
    def __str__(self):
        return self.nome_restaurante