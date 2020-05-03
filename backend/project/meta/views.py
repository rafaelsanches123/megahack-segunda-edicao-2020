from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import MetaModel
from .serializers import MetaSerializer

import os
import io
import json

class MetaView(generics.ListCreateAPIView):
    '''
        Exemplo de POST meta: 127.0.0.1:8000/meta/
    '''
    queryset = MetaModel.objects.all()
    serializer_class = MetaSerializer

    def get(self, request):
        # request
        # http://localhost:8000/meta/?email=fulano@gmail.com
        _json = request.query_params
        if 'email' in _json:
            # pesquisa pela meta do usuário
            query = MetaModel.objects.filter(email=_json['email'])
            if query:
                for p in MetaModel.objects.all():
                    if p.email == _json['email']:
                        return Response(
                            {
                                'message': 'Dados de meta encontrados.',
                                'dados': {   
                                    'descricao': p.descricao, 
                                    'valor': p.valor,
                                    'data_inicial': p.data_inicial,
                                    'data_final': p.data_final
                                }
                            }, status=200)
            return Response({'message': 'Meta não registrada.'}, status=401)
        else:
            return Response({'message': 'Email não informado.'}, status=400)

    def post(self, request):
        _json = request.data
        if not 'email' in _json:
            return Response({'message': 'email não informado.'}, status=400)

        if not 'descricao' in _json:
            return Response({'message': 'descricao não informada.'}, status=400)

        if not 'valor' in _json:
            return Response({'message': 'valor não informado.'}, status=400)

        if not 'data_inicial' in _json:
            return Response({'message': 'data_inicial não informada.'}, status=400)

        if not 'data_final' in _json:
            return Response({'message': 'data_final não informada.'}, status=400)

        data = MetaModel.objects.filter(email=_json['email'])
        if not data:
            MetaModel.objects.filter(email=_json['email']).update(descricao=_json['descricao'])
            MetaModel.objects.filter(email=_json['email']).update(valor=_json['valor'])
            MetaModel.objects.filter(email=_json['email']).update(data_inicial=_json['data_inicial'])
            MetaModel.objects.filter(email=_json['email']).update(data_final=_json['data_final'])
            # registra meta
            # register = MetaModel(
            #     descricao=_json['descricao'],
            #     valor=_json['valor'],
            #     data_inicial=_json['data_inicial'],
            #     data_final=_json['data_final']
            # )
            # register.save()
            return Response({'message': 'Meta registrada com sucesso!'}, status=200)
        else:
            return Response({'message': 'Erro: Meta já cadastrada.'}, status=400)
