# Generated by Django 4.0.3 on 2023-04-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='des',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
