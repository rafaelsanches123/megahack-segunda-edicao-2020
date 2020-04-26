from rest_framework import serializers
from .models import LoginModel

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = LoginModel
        fields = '__all__'