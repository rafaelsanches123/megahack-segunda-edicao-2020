from django.db import models


class CheckingModel(models.Model):
    
    class Meta:
        db_table = 'checking'
    
    cnpj = models.CharField(max_length=40, primary_key=True)
    data = models.CharField(max_length=40)

    def __str__(self):
        return self.cnpj
 