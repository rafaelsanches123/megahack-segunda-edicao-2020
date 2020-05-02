from django.db import migrations, models

from project.cadastro.models import CadastroModel

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaModel',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True)),
                ('valor', models.FloatField()),
                ('descricao', models.TextField()),
                ('data_inicial', models.TextField()),
                ('data_final', models.TextField()),
            ],
            options={
                'db_table': 'meta',
            },
        ),
    ]
