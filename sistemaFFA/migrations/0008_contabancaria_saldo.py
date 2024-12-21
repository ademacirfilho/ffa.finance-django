# Generated by Django 5.1.3 on 2024-12-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaFFA', '0007_contato_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contabancaria',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]