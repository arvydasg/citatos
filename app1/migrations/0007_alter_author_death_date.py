# Generated by Django 3.2.5 on 2021-09-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_quote_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]