# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from random import randint, random

def combine_names(apps, schema_editor):
    RankingModel = apps.get_model("ranking", "RankingModel")
    nomes = [
        'Água Doce Cachaçaria', 
        'SC Restaurante', 
        'Rancho da Picanha', 
        'Niray'
    ]
    numero_estrelas_valor = [randint(1, 5) for _ in range(0, len(nomes))]
    valor_prato = [float(randint(10, 50)) for _ in range(0, len(nomes))]
    numero_estrelas_prato = [randint(1, 5) for _ in range(0, len(nomes))]

    for i in range(0, len(nomes)):
        register = RankingModel(
            nome_restaurante=nomes[i],
            numero_estrelas_prato=numero_estrelas_prato[i],
            valor_prato=valor_prato[i],
            numero_estrelas_valor=numero_estrelas_valor[i]
        )
        register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]