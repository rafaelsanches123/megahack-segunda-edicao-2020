from django.db import models
from django.contrib.postgres.fields import JSONField

class LoginModel(models.Model):
    
    class Meta:
        db_table = 'login'
    
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=10)
    
    def __str__(self):
        return self.usuario