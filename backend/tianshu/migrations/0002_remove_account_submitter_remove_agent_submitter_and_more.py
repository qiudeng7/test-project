# Generated by Django 5.1.3 on 2024-12-05 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tianshu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='platformaccountrecharge',
            name='submitter',
        ),
    ]
