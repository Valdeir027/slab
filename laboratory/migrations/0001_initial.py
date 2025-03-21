# Generated by Django 5.1.7 on 2025-03-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Disponível'), (1, 'Indisponível')], default=0)),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
