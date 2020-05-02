# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def combine_names(apps, schema_editor):
    DicaModel = apps.get_model("dica", "DicaModel")
    descricao = 'Dica do dia: Fique rico com os vídeos da Betina!'
    register = DicaModel(
        descricao=descricao,
    )
    register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('dica', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]