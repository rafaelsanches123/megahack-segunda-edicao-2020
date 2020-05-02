from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import LoginModel
from project.cadastro.models import CadastroModel
from .serializers import LoginSerializer
# from .tasks import function_1

# from celery import shared_task

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
        if not 'email' in _json:
            return Response({'message': 'email não informado.'}, status=400)
        if not 'senha' in _json:
            return Response({'message': 'senha não informada.'}, status=400)
        data = CadastroModel.objects.filter(email=_json['email'])
        # faz login
        if data:
            match = False
            for p in CadastroModel.objects.all():
                if p.senha == _json['senha'] and _json['email'] == p.email:
                    match = True
            if match:
                return Response({'message': 'Login realizado com sucesso!'}, status=200)
            else:
                return Response({'message': 'Erro: Senha incorreta.'}, status=400)
        else:
            return Response({'message': 'Erro: Usuário não cadastrado.'}, status=400)
