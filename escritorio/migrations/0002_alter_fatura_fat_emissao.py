# Generated by Django 5.0.1 on 2024-01-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatura',
            name='fat_emissao',
            field=models.CharField(max_length=15),
        ),
    ]
