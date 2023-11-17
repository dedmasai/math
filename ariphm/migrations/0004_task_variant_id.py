# Generated by Django 4.2.7 on 2023-11-16 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ariphm', '0003_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='variant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ariphm.variant'),
            preserve_default=False,
        ),
    ]
