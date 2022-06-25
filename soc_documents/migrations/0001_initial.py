# Generated by Django 3.2.9 on 2022-06-25 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('soc_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('doc_file', models.FileField(upload_to='minutes/%Y/%F')),
                ('uploaded_by', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('doc_file', models.FileField(upload_to='minutes/%Y/%F')),
                ('uploaded_by', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='meeting', to='soc_events.meeting')),
            ],
            options={
                'verbose_name_plural': 'Minutes',
                'ordering': ('-id',),
            },
        ),
    ]
