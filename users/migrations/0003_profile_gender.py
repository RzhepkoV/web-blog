# Generated by Django 3.1.4 on 2020-12-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201228_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Мужской пол', 'Man'), ('Женский пол', 'Woman')], default='Мужской пол', max_length=11, verbose_name='Выбор пола'),
        ),
    ]
