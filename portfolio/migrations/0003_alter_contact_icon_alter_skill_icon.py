# Generated by Django 4.2.2 on 2023-07-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_delete_backendproject_delete_frontendproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='icon',
            field=models.FileField(upload_to='contact'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.FileField(upload_to='skill'),
        ),
    ]