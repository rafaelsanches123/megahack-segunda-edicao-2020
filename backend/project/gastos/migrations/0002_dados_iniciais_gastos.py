# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def combine_names(apps, schema_editor):
    GastosModel = apps.get_model("gastos", "GastosModel")
    valores = [45.10, 16.95, 34.80, 10.56, 20.00]
    nomes = ['Rancho da Picanha', 'Água Doce Cachaçaria', 'Padaria do Zé', 'PF do Jão', 'SC Restaurante']
    datas = ['30/04/2020', '28/04/2020', '23/04/2020', '15/04/2020', '04/04/2020']

    for i in range(0, len(valores)):
        register = GastosModel(
            nome=nomes[i],
            valor=valores[i],
            data=datas[i]
        )
        register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]