from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import GastosModel
from .serializers import GastosSerializer

import os
import io
import json

class GastosView(generics.ListCreateAPIView):
    '''
        Exemplo de POST gastos: 127.0.0.1:8000/gastos/
    '''
    queryset = GastosModel.objects.all()
    serializer_class = GastosSerializer

    def get(self, request):
        # http://localhost:8000/gastos/
        _json = request.query_params
        gastos = []
        for p in GastosModel.objects.all():
            gastos.append(
                {   
                    'nome': p.nome, 
                    'valor': p.valor,
                    'data': p.data
                })
        return Response({'message': 'Dados de gastos', 'dados': gastos}, status=200)
     
    def post(self, request):
        return Response({'message': 'API com método de POST.'}, status=200)