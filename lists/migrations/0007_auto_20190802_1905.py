# Generated by Django 2.2 on 2019-08-02 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20190802_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]