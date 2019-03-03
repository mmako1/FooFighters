# Generated by Django 2.1.1 on 2019-03-03 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paygroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('venmo_name', models.CharField(blank=True, max_length=500)),
                ('accumulated', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('group', models.ManyToManyField(to='models.Paygroup')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('info', models.TextField(default='')),
                ('dic', models.TextField(default='')),
                ('completed', models.BooleanField(default=False)),
                ('notcompletedlist', models.CharField(default='', max_length=1000)),
                ('completedlist', models.CharField(default='', max_length=1000)),
                ('totlist', models.CharField(default='', max_length=1000)),
                ('venmo_id', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='receipts',
            field=models.ManyToManyField(to='models.Receipt'),
        ),
    ]
