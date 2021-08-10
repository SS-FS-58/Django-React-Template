# Generated by Django 3.1.7 on 2021-04-28 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_business_entity'),
        ('financial_risk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business_conditional_risk',
            name='business_entity_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity'),
        ),
        migrations.AddField(
            model_name='business_structural_risk',
            name='business_entity_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity'),
        ),
        migrations.AddField(
            model_name='business_systemic_risk',
            name='business_entity_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity'),
        ),
        migrations.AddField(
            model_name='hedgeability',
            name='business_entity_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity'),
        ),
        migrations.AddField(
            model_name='risk_weight',
            name='business_entity_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity'),
        ),
        migrations.AlterField(
            model_name='business_conditional_risk',
            name='last_updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='business_structural_risk',
            name='last_updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='business_systemic_risk',
            name='last_updated',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Business_Risk_Assesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_date', models.DateField()),
                ('business_entity_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='business.business_entity')),
            ],
        ),
        migrations.AddField(
            model_name='business_conditional_risk',
            name='business_risk_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financial_risk.business_risk_assesment'),
        ),
        migrations.AddField(
            model_name='business_structural_risk',
            name='business_risk_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financial_risk.business_risk_assesment'),
        ),
        migrations.AddField(
            model_name='business_systemic_risk',
            name='business_risk_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financial_risk.business_risk_assesment'),
        ),
        migrations.AddField(
            model_name='hedgeability',
            name='business_risk_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financial_risk.business_risk_assesment'),
        ),
        migrations.AddField(
            model_name='risk_weight',
            name='business_risk_assessment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financial_risk.business_risk_assesment'),
        ),
    ]