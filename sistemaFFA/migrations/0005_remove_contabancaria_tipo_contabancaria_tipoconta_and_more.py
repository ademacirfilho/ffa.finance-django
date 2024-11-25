# Generated by Django 5.1.3 on 2024-11-25 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaFFA', '0004_conta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contabancaria',
            name='tipo',
        ),
        migrations.AddField(
            model_name='contabancaria',
            name='tipoConta',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sistemaFFA.conta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]