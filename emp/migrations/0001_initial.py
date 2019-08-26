# Generated by Django 2.0.6 on 2019-07-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.SmallIntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('birthday', models.DateField()),
                ('headpic', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
