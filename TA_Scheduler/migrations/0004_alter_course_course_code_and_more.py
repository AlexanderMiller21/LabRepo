# Generated by Django 5.1.4 on 2024-12-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0003_emaillist_alter_course_course_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_instructor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]