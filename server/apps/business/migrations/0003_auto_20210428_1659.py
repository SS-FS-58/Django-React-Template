# Generated by Django 3.1.7 on 2021-04-28 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        ('business', '0002_business_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_entity',
            name='client_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administration.client_entity'),
        ),
        migrations.AlterField(
            model_name='business_entity',
            name='org_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='administration.org_entity'),
        ),
    ]
