# Generated by Django 3.2 on 2024-03-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fazenda', '0002_remove_fazenda_cultura'),
        ('cultura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultura',
            name='fazendas',
            field=models.ManyToManyField(related_name='culturas', to='fazenda.Fazenda'),
        ),
    ]
