# Generated by Django 3.2.7 on 2022-06-02 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_portal', '0005_auto_20220601_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networth',
            old_name='other',
            new_name='other_crypto',
        ),
    ]
