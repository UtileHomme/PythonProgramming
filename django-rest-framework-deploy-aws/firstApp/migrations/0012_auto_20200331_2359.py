# Generated by Django 2.2.5 on 2020-03-31 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0011_auto_20200331_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carspecs',
            name='car_plan',
        ),
        migrations.DeleteModel(
            name='CarPlan',
        ),
    ]