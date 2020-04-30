from rest_framework import serializers
from .models import CadastroModel

class CadastroSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CadastroModel
        fields = '__all__'