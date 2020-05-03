from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import RankingModel
from .serializers import RankingSerializer

import os, io, json

class RankingView(generics.ListCreateAPIView):
    '''
        Exemplo de POST ranking: 127.0.0.1:8000/ranking/
    '''
    queryset = RankingModel.objects.all()
    serializer_class = RankingSerializer
           
    def get(self, request):
        resp = []
        for p in RankingModel.objects.all():
            resp.append({   
                'nome_restaurante': p.nome_restaurante, 
                'valor_prato': p.valor_prato,
                'classificacao': p.numero_estrelas_prato
                # 'numero_estrelas_valor': p.numero_estrelas_valor
            })
        return Response({'message': 'Ranking acessado com sucesso!', 'dados': resp}, status=200)

    def post(self, request):
        _json = request.data
        if not 'nome_restaurante' in _json:
            return Response({'message': 'nome_restaurante não informado.'}, status=400)
        if not 'valor_prato' in _json:
            return Response({'message': 'valor_prato não informada.'}, status=400)
        if not 'numero_estrelas_prato' in _json:
            return Response({'message': 'numero_estrelas_prato não informada.'}, status=400)
        if not 'numero_estrelas_valor' in _json:
            return Response({'message': 'numero_estrelas_valor não informada.'}, status=400)
        register = RankingModel(
            nome_restaurante=_json['nome_restaurante'],
            valor_prato=_json['valor_prato'],
            numero_estrelas_prato=_json['numero_estrelas_prato'],
            numero_estrelas_valor=_json['numero_estrelas_valor']
        )
        register.save()
        return Response({'message': 'Dados cadastrados com sucesso.'}, status=200)
