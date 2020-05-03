# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from random import randint, random

def combine_names(apps, schema_editor):
    CadastroModel = apps.get_model("cadastro", "CadastroModel")
    emails = ['joelsonn.santos@gmail.com', 'rafael.sanches@gmail.com', 'professorarenata@gmail.com']
    senhas = ['123', '123', '123']

    nomes = [
        'Joelson Santos',
        'Rafael Sanches',
        'Renata'
    ]

    apelidos = [
        'Jô',
        'Rafa',
        'Renata'
    ]

    celulares = [
        '38991244980',
        '16999737849',
        '16981236543'
    ]

    rendas = [
        3200.00,
        8500.00,
        10000.00,
    ]

    gastos = [
        1500.00,
        2000.00,
        3500.00
    ]

    for i in range(0, len(nomes)):
        register = CadastroModel(
            email=emails[i],
            senha=senhas[i],
            nome=nomes[i],
            apelido=apelidos[i],
            celular=celulares[i],
            renda=rendas[i],
            gasto=gastos[i]
        )
        register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]