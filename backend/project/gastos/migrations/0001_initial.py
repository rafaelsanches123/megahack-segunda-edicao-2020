from django.db import migrations, models

from project.cadastro.models import CadastroModel

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GastosModel',
            fields=[
                ('nome', models.CharField(max_length=100, primary_key=True)),
                ('valor', models.FloatField()),
                ('data', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gastos',
            },
        ),
    ]
