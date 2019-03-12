# Generated by Django 2.1.2 on 2019-03-12 14:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('irb', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('investigator', models.CharField(max_length=100)),
                ('investigator_phone', models.CharField(max_length=100)),
                ('investigator_email', models.CharField(max_length=100)),
                ('requestor', models.CharField(max_length=100)),
                ('requestor_phone', models.CharField(max_length=100)),
                ('requestor_email', models.EmailField(max_length=100)),
                ('chart_review', models.BooleanField()),
                ('request_type', models.CharField(choices=[('Specialized Counts', 'Specialized Counts'), ('Limited Data Set', 'Limited Data Set'), ('De-Identified Dataset', 'De-Identified Dataset'), ('Identified Dataset', 'Identified Dataset')], default='Identified Dataset', max_length=50)),
                ('date_deadline', models.DateField(default=datetime.date.today)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]