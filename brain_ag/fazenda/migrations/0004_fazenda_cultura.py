# Generated by Django 3.2 on 2024-03-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura', '0002_alter_cultura_table'),
        ('fazenda', '0003_auto_20240310_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='fazenda',
            name='cultura',
            field=models.ManyToManyField(to='cultura.Cultura'),
        ),
    ]