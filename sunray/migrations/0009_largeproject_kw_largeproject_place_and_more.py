# Generated by Django 4.2.10 on 2024-08-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunray', '0008_remove_largeproject_project_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='largeproject',
            name='kw',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='largeproject',
            name='place',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='largeproject',
            name='saves',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='largeproject',
            name='technology',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='largeproject',
            name='tons',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='largeproject',
            name='trees',
            field=models.CharField(default='', max_length=50),
        ),
    ]