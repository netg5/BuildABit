# Generated by Django 2.0.9 on 2018-10-26 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestor', '0005_auto_20181027_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickuprequest',
            name='typechar',
        ),
        migrations.AlterField(
            model_name='pickuprequest',
            name='typeofwaste',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]