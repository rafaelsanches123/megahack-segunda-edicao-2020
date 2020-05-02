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
        '(12)99999-9999',
        '(12)99999-9999',
        '(12)99999-9999'
    ]

    rendas = [
        1000.00,
        1000.00,
        1000.00,
    ]

    gastos = [
        200.00,
        54.00,
        125.80
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