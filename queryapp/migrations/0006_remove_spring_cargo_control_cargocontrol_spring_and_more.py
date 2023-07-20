# Generated by Django 4.2.3 on 2023-07-20 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queryapp', '0005_alter_client_email_alter_spring_eccentricity1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spring',
            name='cargo_control',
        ),
        migrations.AddField(
            model_name='cargocontrol',
            name='spring',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring'),
        ),
        migrations.AlterField(
            model_name='designedspring',
            name='spring',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='samplespring',
            name='spring',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='queryapp.spring'),
        ),
    ]
