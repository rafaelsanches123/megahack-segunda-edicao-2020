from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RankingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_restaurante', models.CharField(max_length=100)),
                ('valor_prato', models.FloatField()),
                ('numero_estrelas_valor', models.IntegerField()),
                ('numero_estrelas_prato', models.IntegerField()),
            ],
            options={
                'db_table': 'ranking',
            },
        ),
    ]
