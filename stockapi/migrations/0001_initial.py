# Generated by Django 3.0.5 on 2020-04-27 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_symbol', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModelStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf', models.FloatField()),
                ('open_price', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('vwap', models.FloatField()),
                ('volume', models.FloatField()),
                ('prev_close', models.FloatField()),
                ('turnover', models.FloatField()),
                ('trans', models.FloatField()),
                ('difference_rs', models.FloatField()),
                ('range_rs', models.FloatField()),
                ('difference_percent', models.FloatField()),
                ('range_percent', models.FloatField()),
                ('vwap_percent', models.FloatField()),
                ('oneeighty_days', models.FloatField()),
                ('fiftytwo_week_high', models.FloatField()),
                ('fiftytwo_week_low', models.FloatField()),
                ('date_added', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.ModelCompany')),
            ],
            options={
                'verbose_name_plural': 'Company stock information',
            },
        ),
        migrations.CreateModel(
            name='ModelDynamicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_bonus_share', models.CharField(max_length=100)),
                ('latest_cash_dividend', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('book_close_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.ModelCompany')),
            ],
        ),
    ]
