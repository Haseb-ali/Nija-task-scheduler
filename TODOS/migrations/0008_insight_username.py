# Generated by Django 3.1.1 on 2021-01-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODOS', '0007_insight'),
    ]

    operations = [
        migrations.AddField(
            model_name='insight',
            name='username',
            field=models.CharField(default=None, max_length=50),
        ),
    ]