# Generated by Django 5.0.6 on 2024-06-05 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wweb", "0002_result_alter_students_contact_alter_students_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="roll_num",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="wweb.students"
            ),
        ),
    ]