# Generated by Django 3.2.9 on 2021-12-20 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AssessmentSystem', '0002_manageproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('expenses_id', models.AutoField(primary_key=True, serialize=False)),
                ('expenses_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='income',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('income_amount', models.IntegerField()),
                ('income_source', models.CharField(max_length=200)),
                ('income_date', models.DateField()),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='plan',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_amount', models.IntegerField()),
                ('plans', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AssessmentSystem.income')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=20)),
                ('profile', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='addproject',
        ),
        migrations.DeleteModel(
            name='manageproject',
        ),
        migrations.AddField(
            model_name='expenses',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssessmentSystem.plan'),
        ),
    ]