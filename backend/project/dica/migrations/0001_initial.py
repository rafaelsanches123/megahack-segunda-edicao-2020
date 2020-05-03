from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DicaModel',
            fields=[
                ('descricao', models.CharField(max_length=200, primary_key=True)),
            ],
            options={
                'db_table': 'dica',
            },
        ),
    ]
