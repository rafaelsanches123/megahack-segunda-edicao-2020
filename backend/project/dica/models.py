from django.db import models
from django.contrib.postgres.fields import JSONField

class DicaModel(models.Model):
    
    class Meta:
        db_table = 'dica'
    
    descricao = models.TextField()
    
    def __str__(self):
        return self.descricao