from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import CadastroModel
from project.meta.models import MetaModel
from .serializers import CadastroSerializer

import os
import io
import json

class CadastroView(generics.ListCreateAPIView):
    '''
        Exemplo de POST cadastro: 127.0.0.1:8000/cadastro/
    '''
    queryset = CadastroModel.objects.all()
    serializer_class = CadastroSerializer

    def get(self, request):
        # request
        # http://localhost:8000/cadastro/?email=fulano@gmail.com
        _json = request.query_params
        if 'email' in _json:
            # pesquisa pelo usuário
            query = CadastroModel.objects.filter(email=_json['email'])
            if query:
                for p in CadastroModel.objects.all():
                    if p.email == _json['email']:
                        return Response(
                            {   
                                'renda': p.renda, 
                                'gasto': p.gasto,
                                'apelido': p.apelido,
                                'celular': p.celular,
                                'nome': p.nome
                            }, status=200)
            return Response({'message': 'Usuário não identificado'}, status=401)
        else:
            return Response({'message': 'Email não informado'}, status=401)

    def post(self, request):
        _json = request.data
        if not 'nome' in _json:
            return Response({'message': 'nome não informado.'}, status=400)

        if not 'senha' in _json:
            return Response({'message': 'senha não informada.'}, status=400)

        if not 'apelido' in _json:
            return Response({'message': 'apelido não informado.'}, status=400)

        if not 'renda' in _json:
            return Response({'message': 'renda não informada.'}, status=400)

        if not 'email' in _json:
            return Response({'message': 'email não informado.'}, status=400)

        if not 'gasto' in _json:
            return Response({'message': 'gastos não informado.'}, status=400)

        if not 'celular' in _json:
            return Response({'message': 'celular não informado.'}, status=400)

        data = CadastroModel.objects.filter(email=_json['email'])

        if not data:
            # faz cadastro
            register = CadastroModel(
                nome=_json['nome'],
                senha=_json['senha'],
                apelido=_json['apelido'],
                gasto=_json['gasto'],
                renda=_json['renda'],
                email=_json['email'],
                celular=_json['celular']
            )
            register.save()
            meta = MetaModel(
                descricao='',
                email=_json['email'],
                valor=0.00,
                data_inicial='',
                data_final=''
            )
            meta.save()
            return Response({'message': 'Cadastro realizado com sucesso!'}, status=200)
        else:
            return Response({'message': 'Erro: Usuário já cadastrado.'}, status=400)
