from django.db import models
from django.contrib.postgres.fields import JSONField

class LoginModel(models.Model):
    
    class Meta:
        db_table = 'login'
    user = models.TextField()
    password = models.TextField()
    
    def __str__(self):
        return self.user