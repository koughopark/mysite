# Generated by Django 2.0.6 on 2018-07-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_regdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='name',
            field=models.CharField(default=' ', max_length=10),
        ),
    ]
