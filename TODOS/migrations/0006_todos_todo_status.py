# Generated by Django 3.1.1 on 2021-01-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOS', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='todo_status',
            field=models.CharField(default='uncompleted', max_length=50),
        ),
    ]
