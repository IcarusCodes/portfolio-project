# Generated by Django 2.2 on 2019-05-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190502_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]