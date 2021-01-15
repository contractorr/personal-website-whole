# Generated by Django 3.1.4 on 2021-01-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputsContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_amount', models.FloatField(default=5000)),
                ('cagr', models.FloatField(default=20)),
                ('num_years', models.IntegerField(default=20)),
                ('beginning_year', models.IntegerField(default=2021)),
                ('annual_topup', models.FloatField(default=1000)),
                ('topup_years', models.IntegerField(default=5)),
            ],
        ),
    ]