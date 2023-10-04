# Generated by Django 4.2.5 on 2023-10-04 18:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('solicitation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='solicitation.solicitation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
