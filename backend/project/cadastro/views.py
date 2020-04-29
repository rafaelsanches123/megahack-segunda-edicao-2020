from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import CadastroModel
from .serializers import CadastroSerializer

import os, io, json
import uuid

class CadastroView(generics.ListCreateAPIView):
    '''
        Exemplo de POST login: 127.0.0.1:8000/cadastro/
    '''
    queryset = CadastroModel.objects.all()
    serializer_class = CadastroSerializer
           
    def get(self, request):
        return Response({'message': 'Método GET'}, status=200)
        
    def post(self, request):
        _json = request.data
        data = CadastroModel.objects.filter(user=_json['usuario'])
        if not data:
            # faz cadastro
            register = CadastroModel(
                usuario=_json['usuario'], 
                nome=_json['nome'],
                senha=_json['senha'],
                apelido=_json['apelido'],
                renda=_json['renda'],
                email=_json['email'],
                celular=_json['celular']
            )
            register.save()
            return Response({'message': 'Cadastro realizado com sucesso!'}, status=200)
        else:
            return Response({'message': 'Erro: Usuário já cadastrado.'}, status=400)