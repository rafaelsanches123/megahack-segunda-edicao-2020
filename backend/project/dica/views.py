from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import DicaModel
from .serializers import DicaSerializer

import os
import io
import json

class DicaView(generics.ListCreateAPIView):
    '''
        Exemplo de POST dica: 127.0.0.1:8000/dica/
    '''
    queryset = DicaModel.objects.all()
    serializer_class = DicaSerializer

    def get(self, request):
        # request
        # http://localhost:8000/dica/
        dicas = []
        for p in DicaModel.objects.all():
            dicas.append(
                {   
                    'descricao': p.descricao
                })
        return Response({'message': 'Dicas recuperadas com sucesso', 'dados': dicas}, status=401)

    def post(self, request):
        _json = request.data
        if not 'descricao' in _json:
            return Response({'message': 'descricao não informada.'}, status=400)
        # registra dica
        register = DicaModel(
            descricao=_json['descricao']
        )
        register.save()
        return Response({'message': 'Dica registrada com sucesso!'}, status=200)