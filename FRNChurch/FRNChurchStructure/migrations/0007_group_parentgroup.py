# Generated by Django 2.2.5 on 2019-10-10 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0006_auto_20191010_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='parentGroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FRNChurchStructure.Group'),
        ),
    ]