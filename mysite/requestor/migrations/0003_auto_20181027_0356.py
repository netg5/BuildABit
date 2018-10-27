# Generated by Django 2.0.9 on 2018-10-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0002_auto_20181027_0036'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Collector',
        ),
        migrations.DeleteModel(
            name='Requestor',
        ),
        migrations.RemoveField(
            model_name='pickuprequest',
            name='pickup_date',
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='request_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
