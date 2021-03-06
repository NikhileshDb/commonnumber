# Generated by Django 3.1.6 on 2021-02-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonnumber', '0003_auto_20210221_0458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commonnumber',
        ),
        migrations.AlterField(
            model_name='teerresult',
            name='commonnumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teerresult',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teerresult',
            name='firstresult',
            field=models.IntegerField(blank=True, null=True, verbose_name='FR'),
        ),
        migrations.AlterField(
            model_name='teerresult',
            name='secondresult',
            field=models.IntegerField(blank=True, null=True, verbose_name='SR'),
        ),
    ]
