# Generated by Django 3.2.9 on 2022-06-10 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soc_members', '0008_member_full_name'),
        ('soc_documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutes',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='minutes', to='soc_members.member'),
        ),
    ]