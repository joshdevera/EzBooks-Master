# Generated by Django 2.2.6 on 2019-10-23 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191021_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user_profile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='major',
            field=models.CharField(default='Undecided', max_length=100),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]