# Generated by Django 5.0.1 on 2024-01-26 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0004_alter_pagamento_pag_idgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroMulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_multa', models.FloatField()),
                ('data_aplicacao', models.DateField()),
                ('fatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escritorio.fatura')),
            ],
        ),
    ]
