# Generated by Django 3.2 on 2024-03-15 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produtor',
            options={'ordering': ['nome'], 'verbose_name': 'brain_ag_produtor', 'verbose_name_plural': 'Produtores'},
        ),
    ]
