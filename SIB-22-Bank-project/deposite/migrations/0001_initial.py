# Generated by Django 4.1.3 on 2022-11-14 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_accounttype_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_deposite', models.DecimalField(decimal_places=2, max_digits=12)),
                ('deposite_type', models.PositiveSmallIntegerField(choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Interest')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposite', to='accounts.useraccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
