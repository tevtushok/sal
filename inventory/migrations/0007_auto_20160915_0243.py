# Generated by Django 1.10 on 2016-09-15 09:43


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20160909_1448'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('name', 'bundleid', 'bundlename')]),
        ),
    ]
