# Generated by Django 3.2.3 on 2021-05-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]