# Generated by Django 5.0.1 on 2024-01-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0008_remove_fatura_fat_vencimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatura',
            name='fat_vencimento',
            field=models.DateField(default='2000-01-01'),
        ),
    ]