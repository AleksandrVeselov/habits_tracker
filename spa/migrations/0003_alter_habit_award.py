# Generated by Django 4.2.4 on 2023-08-25 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0002_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='award',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознаграждение'),
        ),
    ]
