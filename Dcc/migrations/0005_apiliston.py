# Generated by Django 3.0.8 on 2020-07-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dcc', '0004_reportlist_reportclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='apiliston',
            fields=[
                ('item', models.CharField(max_length=128)),
                ('release', models.CharField(max_length=128)),
                ('modules', models.CharField(max_length=128)),
                ('casename', models.CharField(max_length=500)),
                ('caselists', models.CharField(max_length=1000)),
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '抖查查线上接口用例',
                'verbose_name_plural': '抖查查线上接口用例',
                'ordering': ['-c_time'],
            },
        ),
    ]