# Generated by Django 4.2.4 on 2023-08-23 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='Место')),
                ('habit_time', models.TimeField()),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField()),
                ('periodicity', models.IntegerField(verbose_name='Периодичность')),
                ('award', models.CharField(max_length=255, verbose_name='Вознаграждение')),
                ('execution_time', models.DurationField(verbose_name='Время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичность')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spa.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
