# Generated by Django 3.0.7 on 2020-06-07 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200607_1145'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='public"."posts_table',
        ),
    ]