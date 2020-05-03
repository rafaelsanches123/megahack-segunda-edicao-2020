from django.db import models
from django.contrib.postgres.fields import JSONField

class DicaModel(models.Model):
    
    class Meta:
        db_table = 'dica'
    
    descricao = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.descricao