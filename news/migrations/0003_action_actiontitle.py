# Generated by Django 2.1.2 on 2018-10-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20181006_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='actionTitle',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
