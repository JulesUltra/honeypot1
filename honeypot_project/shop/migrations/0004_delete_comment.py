# Generated by Django 3.2.12 on 2022-03-05 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_comment_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
