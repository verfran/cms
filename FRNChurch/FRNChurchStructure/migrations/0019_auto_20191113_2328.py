# Generated by Django 2.2.5 on 2019-11-13 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0018_auto_20191113_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='contact',
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
