# Generated by Django 2.2 on 2019-05-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='relevant_skills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='time_period',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
