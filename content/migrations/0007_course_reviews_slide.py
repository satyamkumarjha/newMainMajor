# Generated by Django 3.0.6 on 2021-05-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_course_reviews_reviewer_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_reviews',
            name='slide',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
