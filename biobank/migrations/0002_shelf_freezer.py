# Generated by Django 4.1 on 2022-08-22 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("biobank", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelf",
            name="freezer",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="biobank.freezer",
            ),
            preserve_default=False,
        ),
    ]
