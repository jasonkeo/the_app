# Generated by Django 4.2.16 on 2024-10-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('market_data', models.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='index',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.TextField(),
        ),
    ]
