# Generated by Django 2.2 on 2019-11-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('id_fournisseur', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('adress', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code', models.FloatField(blank=True, null=True)),
                ('siren', models.FloatField(blank=True, null=True)),
                ('user_username', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
