from rest_framework import serializers
from .models import RankingModel

class RankingSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = RankingModel
        fields = '__all__'