# Generated by Django 3.2.9 on 2022-06-14 17:23

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soc_finance', '0004_auto_20220614_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine_type', models.CharField(choices=[(None, 'Select fine type'), ('meeting absence', 'Meeting Absence'), ('funeral absence', 'Funeral Absence'), ('late coming', 'Late Coming'), ('uniform', 'Uniform'), ('disciplinary action', 'Disciplinary Action')], max_length=300)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('topup_type', models.CharField(choices=[(None, 'Select top-up type'), ('funeral topup', 'Funeral Topup'), ('transport augmentation', 'Transport Augmentation'), ('special function', 'Special Function')], max_length=250)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='member',
        ),
        migrations.RemoveField(
            model_name='memberaccount',
            name='other_debits',
        ),
        migrations.AddField(
            model_name='memberaccount',
            name='fines',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='memberaccount',
            name='topups',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='memberaccount',
            name='adjustments',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='memberaccount',
            name='cash_deposits',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Debit',
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
        migrations.AddField(
            model_name='topup',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='member_topups', to='soc_finance.memberaccount'),
        ),
        migrations.AddField(
            model_name='fine',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='member_fines', to='soc_finance.memberaccount'),
        ),
    ]
