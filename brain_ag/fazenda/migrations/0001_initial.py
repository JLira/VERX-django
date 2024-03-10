# Generated by Django 3.2 on 2024-03-10 02:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fazenda',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=2)),
                ('area_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area_agricultavel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area_vegetacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produtor', models.ManyToManyField(to='produtor.Produtor')),
            ],
        ),
    ]