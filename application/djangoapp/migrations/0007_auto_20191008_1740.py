# Generated by Django 2.2.6 on 2019-10-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_auto_20191008_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Prenom',
            field=models.CharField(max_length=200),
        ),
    ]
