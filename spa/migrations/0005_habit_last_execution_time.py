# Generated by Django 4.2.4 on 2023-08-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_alter_habit_habit_time_alter_habit_is_pleasant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='last_execution_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время последнего выполнения привычки'),
        ),
    ]
