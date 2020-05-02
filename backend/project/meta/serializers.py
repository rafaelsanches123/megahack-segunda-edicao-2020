from rest_framework import serializers
from .models import MetaModel

class MetaSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = MetaModel
        fields = '__all__'