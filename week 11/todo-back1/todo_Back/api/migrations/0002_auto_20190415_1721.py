# Generated by Django 2.2 on 2019-04-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Task1',
        ),
        migrations.RenameModel(
            old_name='TaskList',
            new_name='TaskList1',
        ),
    ]
