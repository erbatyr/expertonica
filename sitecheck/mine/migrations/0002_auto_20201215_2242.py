# Generated by Django 3.0.6 on 2020-12-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='timeout',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
