# Generated by Django 2.2.13 on 2020-06-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200619_0556"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="kuoiuiou",),
        migrations.RemoveField(model_name="customtext", name="ngjgfjhg",),
        migrations.AddField(
            model_name="homepage",
            name="jhtjhgjhg",
            field=models.URLField(blank=True, null=True),
        ),
    ]
