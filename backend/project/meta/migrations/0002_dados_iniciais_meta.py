# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from random import randint, random

def combine_names(apps, schema_editor):
    MetaModel = apps.get_model("meta", "MetaModel")
    emails = ['joelsonn.santos@gmail.com', 'rafael.sanches@gmail.com', 'professorarenata@gmail.com']
    valores = [300.00, 500.00, 450.00]
    datas_iniciais = ['04/05/2020', '04/05/2020', '04/05/2020']
    datas_finais = ['05/05/2021', '04/05/2021', '04/05/2021']
    descricao = ['Comprar BMW 328i', 'Comprar um Kamikasi', 'Comprar uma Mercedez']

    for i in range(0, len(emails)):
        register = MetaModel(
            email=emails[i],
            valor=valores[i],
            descricao=descricao[i],
            data_inicial=datas_iniciais[i],
            data_final=datas_finais[i]
        )
        register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]