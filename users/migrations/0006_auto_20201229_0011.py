# Generated by Django 3.1.4 on 2020-12-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201228_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Man', 'Мужской пол'), ('Woman', 'Женский пол')], default='Man', max_length=11, verbose_name='Выбор пола'),
        ),
    ]
