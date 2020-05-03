from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckingModel',
            fields=[
                ('cnpj', models.CharField(max_length=40, primary_key=True)),
                ('data', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'checking',
            },
        ),
    ]
