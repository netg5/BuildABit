# Generated by Django 2.0.9 on 2018-10-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0003_auto_20181027_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuprequest',
            name='typeofwaste',
            field=models.CharField(max_length=50),
        ),
    ]
