# Generated by Django 4.1.5 on 2023-01-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "prediction",
            "0012_remove_predictiontable_hey_alter_predictiontable_age_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictiontable",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]