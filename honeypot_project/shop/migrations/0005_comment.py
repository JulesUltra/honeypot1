# Generated by Django 3.2.12 on 2022-03-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('poster', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now=True)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
    ]