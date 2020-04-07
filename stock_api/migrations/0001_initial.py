# Generated by Django 3.0.5 on 2020-04-07 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyStockInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_transactions', models.IntegerField()),
                ('maximum', models.FloatField()),
                ('minimum', models.FloatField()),
                ('closing', models.FloatField()),
                ('traded_shares', models.FloatField()),
                ('amount', models.FloatField()),
                ('previous_closing', models.FloatField()),
                ('difference_rs', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_api.CompanyModel')),
            ],
        ),
    ]