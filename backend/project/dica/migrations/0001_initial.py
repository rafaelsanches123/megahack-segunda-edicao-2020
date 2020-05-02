from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DicaModel',
            fields=[
                ('descricao', models.TextField()),
            ],
            options={
                'db_table': 'dica',
            },
        ),
    ]
