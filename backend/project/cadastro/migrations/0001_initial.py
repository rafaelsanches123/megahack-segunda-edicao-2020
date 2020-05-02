from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroModel',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True)),
                ('senha', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=15)),
                ('renda', models.FloatField()),
                ('gasto', models.FloatField()),
            ],
            options={
                'db_table': 'cadastro',
            },
        ),
    ]
