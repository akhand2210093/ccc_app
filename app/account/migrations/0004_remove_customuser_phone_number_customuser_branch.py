# Generated by Django 4.2.7 on 2024-03-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customuser_branch_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
