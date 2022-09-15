# Generated by Django 4.1.1 on 2022-09-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('sobrenome', models.CharField(max_length=120)),
                ('cpf', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=120)),
                ('bairro', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=200)),
            ],
        ),
    ]