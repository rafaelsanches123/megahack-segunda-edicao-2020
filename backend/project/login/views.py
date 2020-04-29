from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import LoginModel
from .models import CadastroModel
from .serializers import LoginSerializer
from .tasks import function_1

from celery import shared_task

import os, io, json
import uuid


class LoginView(generics.ListCreateAPIView):
    '''
        Exemplo de POST login: 127.0.0.1:8000/login/
    '''
    queryset = LoginModel.objects.all()
    serializer_class = LoginSerializer
           
    def get(self, request):
        return Response({'message': 'Método GET'}, status=200)
        
    def post(self, request):
        _json = request.data
        data = CadastroModel.objects.filter(user=_json['usuario'])
        # faz login
        if data:
            # register = LoginModel(user=_json['user'], password=_json['password'])
            # register.save()
            return Response({'message': 'Login realizado com sucesso!'}, status=200)
        else:
            return Response({'message': 'Erro: Usuário não cadastrado.'}, status=400)