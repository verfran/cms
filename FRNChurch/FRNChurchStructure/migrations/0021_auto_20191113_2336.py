# Generated by Django 2.2.5 on 2019-11-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0020_auto_20191113_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
