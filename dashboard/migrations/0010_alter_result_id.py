# Generated by Django 3.2.7 on 2021-10-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_inputentry_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
