# Generated by Django 2.0.6 on 2019-07-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('realname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
