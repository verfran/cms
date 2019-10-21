# Generated by Django 2.2.5 on 2019-10-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FRNChurchStructure', '0007_group_parentgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('secondName', models.CharField(max_length=30, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Christian',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='FRNChurchStructure.Person')),
                ('dateOfBaptism', models.DateField()),
                ('familyGroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FRNChurchStructure.Group')),
            ],
            bases=('FRNChurchStructure.person',),
        ),
    ]
