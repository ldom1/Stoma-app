# Generated by Django 2.2 on 2020-01-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan_nettoyage', '0004_plannettoyage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannettoyage',
            name='user_username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
