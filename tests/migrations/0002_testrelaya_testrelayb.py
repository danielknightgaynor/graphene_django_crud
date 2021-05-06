# Generated by Django 3.2.1 on 2021-05-05 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gdc_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRelayB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestRelayA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('test_relay_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_relay_as', to='gdc_test.testrelayb')),
            ],
        ),
    ]
