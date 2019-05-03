# Generated by Django 2.2 on 2019-05-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(null=True)),
                ('logo', models.ImageField(null=True, upload_to='images/')),
                ('technologies_used', models.TextField(null=True)),
            ],
        ),
    ]
