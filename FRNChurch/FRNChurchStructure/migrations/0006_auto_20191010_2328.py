# Generated by Django 2.2.5 on 2019-10-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0005_delete_groupgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
