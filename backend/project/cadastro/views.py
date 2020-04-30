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
        if not 'usuario' in _json:
            return Response({'message': 'usuario não informado.'}, status=400)
        if not 'senha' in _json:
            return Response({'message': 'senha não informada.'}, status=400)
        if not 'nome' in _json:
            return Response({'message': 'nome não informado.'}, status=400)
        if not 'apelido' in _json:
            return Response({'message': 'apelido não informado.'}, status=400)
        if not 'renda' in _json:
            return Response({'message': 'renda não informada.'}, status=400)
        if not 'email' in _json:
            return Response({'message': 'email não informado.'}, status=400)
        if not 'celular' in _json:
            return Response({'message': 'celular não informado.'}, status=400)
        data = CadastroModel.objects.filter(usuario=_json['usuario'])
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