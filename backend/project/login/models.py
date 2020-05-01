from django.db import models
from django.contrib.postgres.fields import JSONField

class LoginModel(models.Model):
    
    class Meta:
        db_table = 'login'
    
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email