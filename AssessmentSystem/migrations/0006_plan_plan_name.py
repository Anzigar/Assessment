# Generated by Django 3.2.9 on 2022-01-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssessmentSystem', '0005_plan_plan_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_name',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
