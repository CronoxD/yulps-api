# Generated by Django 2.2.3 on 2019-07-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='is_entry',
        ),
        migrations.AddField(
            model_name='movementcategory',
            name='is_entry',
            field=models.BooleanField(default=False),
        ),
    ]