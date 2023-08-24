# Generated by Django 4.2.3 on 2023-07-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryapp', '0006_alter_spring_eccentricity1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spring',
            name='coil_direction',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='spring',
            name='coils',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='spring',
            name='diam_ext1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='spring',
            name='diam_ext2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='spring',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='spring',
            name='luz1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='spring',
            name='luz2',
            field=models.IntegerField(default=0),
        ),
    ]