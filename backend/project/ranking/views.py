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
        ordered = RankingModel.objects.order_by('-classificacao')
        for p in ordered:
            resp.append({   
                'nome_restaurante': p.nome_restaurante, 
                'valor_prato': p.valor_prato,
                'classificacao': p.classificacao
            })
        return Response({'message': 'Ranking acessado com sucesso!', 'dados': resp}, status=200)

    def post(self, request):
        _json = request.data
        if not 'nome_restaurante' in _json:
            return Response({'message': 'nome_restaurante não informado.'}, status=400)
        if not 'valor_prato' in _json:
            return Response({'message': 'valor_prato não informada.'}, status=400)
        if not 'classificacao' in _json:
            return Response({'message': 'classificacao não informada.'}, status=400)
        register = RankingModel(
            nome_restaurante=_json['nome_restaurante'],
            valor_prato=_json['valor_prato'],
            classificacao=_json['classificacao']
        )
        register.save()
        return Response({'message': 'Dados cadastrados com sucesso.'}, status=200)
