# Generated by Django 3.0.8 on 2020-07-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dcc', '0003_reportlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportlist',
            name='reportclass',
            field=models.CharField(default='', max_length=128),
        ),
    ]
