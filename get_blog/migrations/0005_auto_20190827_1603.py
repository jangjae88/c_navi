# Generated by Django 2.2.4 on 2019-08-27 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_blog', '0004_auto_20190827_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchresult',
            old_name='keyword',
            new_name='search_keyword',
        ),
    ]