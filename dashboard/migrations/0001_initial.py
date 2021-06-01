# Generated by Django 3.0.6 on 2021-03-30 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0005_auto_20201130_2201'),
        ('quiz', '0005_question_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('college', models.CharField(max_length=300)),
                ('branch', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=11)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('courses', models.TextField()),
                ('username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='quiz_scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('course_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='content.course')),
                ('quiz_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='quiz.quiz')),
                ('username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='courses_enrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='quiz.quiz')),
                ('username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]