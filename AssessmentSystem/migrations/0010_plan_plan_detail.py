# Generated by Django 4.0.1 on 2022-01-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssessmentSystem', '0009_remove_income_id_remove_users_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_detail',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
