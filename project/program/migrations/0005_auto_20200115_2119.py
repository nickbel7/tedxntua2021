# Generated by Django 2.2.6 on 2020-01-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20191107_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('G', 'General'), ('T', 'Talk'), ('P', 'Performance'), ('S', 'Side event'), ('H', 'Hosting')], max_length=1, verbose_name='Type'),
        ),
    ]
