from rest_framework import serializers
from .models import GastosModel

class GastosSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = GastosModel
        fields = '__all__'