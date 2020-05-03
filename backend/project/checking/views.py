from __future__ import absolute_import, unicode_literals

from rest_framework import generics
from rest_framework.response import Response
from .models import CheckingModel
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
        # request
        # http://localhost:8000/checking/?cnpj=61.664.102/0001-04
        _json = request.query_params
        if 'cnpj' in _json:
            # pesquisa pelo parceiro
            query = CheckingModel.objects.filter(cnpj=_json['cnpj'])
            if query:
                for p in CheckingModel.objects.all():
                    if p.cnpj == _json['cnpj']:
                        return Response({'message': 'Checking realizado com sucesso!'}, status=200)
            return Response({'message': 'Ocorreu um erro no checking!'}, status=401)
        else:
            return Response({'message': 'Informe o cnpj do parceiro.'}, status=401)

    def post(self, request):
        _json = request.data
        if not 'cnpj' in _json:
            return Response({'message': 'cnpj não informado.'}, status=400)
        if not 'data' in _json:
            return Response({'message': 'data não informada.'}, status=400)
        data = CheckingModel.objects.filter(cnpj=_json['cnpj'])

        if not data:
            # faz cadastro
            register = CheckingModel(
                nome=_json['cnpj'],
                senha=_json['data']
            )
            register.save()
            return Response({'message': 'Cadastro realizado com sucesso!'}, status=200)
        else:
            return Response({'message': 'Erro: CNPJ já cadastrado.'}, status=400)
