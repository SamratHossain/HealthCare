# Generated by Django 3.2.13 on 2022-05-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_remove_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
