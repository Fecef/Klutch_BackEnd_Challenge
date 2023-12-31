# Generated by Django 3.2.22 on 2023-10-07 23:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fee_rate', models.FloatField()),
                ('partner_comission', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
