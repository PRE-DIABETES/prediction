# Generated by Django 4.1.5 on 2023-01-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0006_rename_n1_predictiontable_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictiontable",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]