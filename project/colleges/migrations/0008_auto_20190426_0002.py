# Generated by Django 2.1.5 on 2019-04-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0007_auto_20190425_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='contact1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='contact2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='contact3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course5',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course6',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='course7',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='facility1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='facility2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='facility3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='facility4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='college',
            name='facility5',
            field=models.CharField(max_length=1000),
        ),
    ]