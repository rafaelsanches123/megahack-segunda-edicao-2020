from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import CheckingModel
from project.gastos.models import GastosModel
from .serializers import CheckingSerializer

import os
import io
import json

class CheckingView(generics.ListCreateAPIView):
    '''
        Exemplo de POST cheking: 127.0.0.1:8000/cheking/
    '''
    queryset = CheckingModel.objects.all()
    serializer_class = CheckingSerializer

    def get(self, request):
        return Response({'message': 'API de GET!'}, status=200)
       
    def post(self, request):
        _json = request.data
        if not 'nome' in _json:
            return Response({'message': 'nome não informado.'}, status=400)
        if not 'data' in _json:
            return Response({'message': 'data não informada.'}, status=400)
        if not 'valor' in _json:
            return Response({'message': 'valor não informado.'}, status=400)
        register = GastosModel(
            nome=_json['nome'],
            valor=_json['valor'],
            data=_json['data']
        )
        register.save()
        return Response({'message': 'Checking realizado com sucesso!'}, status=200)
        