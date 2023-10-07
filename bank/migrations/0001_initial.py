# Generated by Django 3.2.22 on 2023-10-07 23:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('agency', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
