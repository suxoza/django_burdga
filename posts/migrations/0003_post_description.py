# Generated by Django 4.2.1 on 2023-05-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.CharField(default="", max_length=100),
        ),
    ]
