# Generated by Django 2.2.5 on 2019-11-22 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0025_auto_20191123_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parentGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FRNChurchStructure.Group'),
        ),
    ]
