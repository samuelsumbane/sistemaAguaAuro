# Generated by Django 5.0.1 on 2024-01-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_username', models.CharField(max_length=30)),
                ('user_nivel', models.CharField(max_length=10)),
                ('user_key', models.IntegerField()),
                ('user_pass', models.CharField(max_length=100)),
                ('user_status', models.BooleanField()),
            ],
        ),
    ]
