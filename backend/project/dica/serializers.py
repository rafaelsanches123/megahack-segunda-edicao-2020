from rest_framework import serializers
from .models import DicaModel

class DicaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = DicaModel
        fields = '__all__'