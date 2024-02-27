# Generated by Django 4.0 on 2024-02-27 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('priority', models.CharField(choices=[(3, 'High'), (2, 'Medium'), (1, 'Low')], max_length=2)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.executor')),
                ('projects', models.ManyToManyField(to='project.Project')),
            ],
        ),
    ]