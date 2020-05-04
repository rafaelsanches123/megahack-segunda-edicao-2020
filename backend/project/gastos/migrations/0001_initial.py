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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('data', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gastos',
            },
        ),
    ]
