from rest_framework import serializers
from .models import CheckingModel

class CheckingSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CheckingModel
        fields = '__all__'