import requests, json, time
from random import randint, random

restaurantes = [
    'Água Doce Cachaçaria', 
    'SC Restaurante', 
    'Rancho da Picanha', 
    'Niray'
]
num_valores = [randint(1, 5) for _ in range(0, len(restaurantes))]
valores = [float(randint(10, 50)) for _ in range(0, len(restaurantes))]
num_qualidades = [randint(1, 5) for _ in range(0, len(restaurantes))]

for i in range(0, len(restaurantes)):
    data = {
        'nome_restaurante': restaurantes[i],
        'numero_estrelas_prato': num_qualidades[i],
        'numero_estrelas_valor': num_valores[i],
        'valor_prato': valores[i]
    }
    resp = requests.post(url='http://localhost:8000/ranking/', data=data)
    print(resp.status_code)





