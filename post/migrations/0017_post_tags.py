# Generated by Django 3.0.4 on 2020-03-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_remove_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]