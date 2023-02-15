# Generated by Django 4.1.5 on 2023-02-14 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_role', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise', models.CharField(max_length=35)),
                ('duration', models.CharField(max_length=30)),
                ('id_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.role')),
            ],
        ),
    ]
