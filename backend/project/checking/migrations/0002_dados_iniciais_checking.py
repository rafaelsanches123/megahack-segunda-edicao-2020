# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def combine_names(apps, schema_editor):
    CheckingModel = apps.get_model("checking", "CheckingModel")
    cnpjs = ['61.664.102/0001-04']
    datas = ['04/05/2020']

    for i in range(0, len(cnpjs)):
        register = CheckingModel(
            cnpj=cnpjs[i],
            data=datas[i]
        )
        register.save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('checking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]