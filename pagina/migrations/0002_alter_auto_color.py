# Generated by Django 5.0.2 on 2024-02-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]
