# Generated by Django 3.2.22 on 2023-10-08 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate_table', '0001_initial'),
        ('solicitation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitation',
            name='rate_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_table.ratetable'),
        ),
    ]
