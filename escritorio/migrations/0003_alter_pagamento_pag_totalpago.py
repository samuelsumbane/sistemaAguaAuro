# Generated by Django 5.0.1 on 2024-01-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0002_alter_fatura_fat_emissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='pag_totalpago',
            field=models.FloatField(null=True),
        ),
    ]
