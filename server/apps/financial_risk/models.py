from django.db import models

from apps.business.models import Business_Entity, Business_Basic_Info, Business_Condition,\
    Business_Finance, Business_Preference


class Business_Risk_Assesment(models.Model):
    assessment_date = models.DateField(auto_now=False, auto_now_add=False)
    # FK fields
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)


class Risk_Weight(models.Model):
    # own variable area.
    risk_weight_coefficient = models.CharField(max_length=50)

    # foreign key area.
    business_risk_assessment = models.ForeignKey(Business_Risk_Assesment, on_delete=models.CASCADE, default=None)
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)


class Business_Systemic_Risk(models.Model):
    # own variable area.
    broader_index_risk_level = models.CharField(max_length=50)
    sector_index_risk_level = models.CharField(max_length=50)
    broader_index_correlation_level = models.CharField(max_length=50)
    sector_index_correlation_level = models.CharField(max_length=50)
    contrarian_level = models.CharField(max_length=50)
    macro_risk_level = models.CharField(max_length=50)
    sector_rotation_risk_level = models.CharField(max_length=50)
    last_updated = models.DateField(auto_now=False, auto_now_add=False)

    # foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(
        Business_Basic_Info, on_delete=models.CASCADE, null=True)
    business_risk_assessment = models.ForeignKey(Business_Risk_Assesment, on_delete=models.CASCADE, default=None)
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)


class Business_Structural_Risk(models.Model):
    # own variable area.
    tech_transformation_risk_level = models.CharField(max_length=50)
    seasonality_risk_level = models.CharField(max_length=50)
    new_vs_old_economy = models.CharField(max_length=50)
    geopolitical_risk_level = models.CharField(max_length=50)
    policy_risk_level = models.CharField(max_length=50)
    product_competitiveness_risk_level = models.CharField(max_length=50)
    business_DNA_risk_level = models.CharField(max_length=50)
    contrarian_level = models.CharField(max_length=50)
    overproduction_risk_level = models.CharField(max_length=50)
    last_updated = models.DateField(auto_now=False, auto_now_add=False)

    # foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(
        Business_Basic_Info, on_delete=models.CASCADE)
    business_risk_assessment = models.ForeignKey(Business_Risk_Assesment, on_delete=models.CASCADE, default=None)
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)


class Business_Conditional_Risk(models.Model):
    # own variable area.
    total_conditional_event_risk_level = models.CharField(max_length=50)
    total_event_correlation_risk_level = models.CharField(max_length=50)
    total_new_competition_risk_level = models.CharField(max_length=50)
    total_new_opportunity_risk_level = models.CharField(max_length=50)
    last_updated = models.DateField(auto_now=False, auto_now_add=False)

    # foreign key area.
    risk_weight_id = models.ForeignKey(Risk_Weight, on_delete=models.CASCADE)
    business_basic_info_id = models.OneToOneField(
        Business_Basic_Info, on_delete=models.CASCADE)
    business_risk_assessment = models.ForeignKey(Business_Risk_Assesment, on_delete=models.CASCADE, default=None)
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)


class Hedgeability(models.Model):
    # own variable area.
    risk_clarity_level = models.CharField(max_length=50)
    risk_quantifiability_level = models.CharField(max_length=50)
    free_cash_liquidity = models.CharField(max_length=50)
    risk_hedge_correlation_clarity_level = models.CharField(max_length=50)
    risk_hedge_correlation_quantifiability_level = models.CharField(
        max_length=50)
    overall_hedgeability_level = models.CharField(max_length=50)

    # foreign key area.
    business_systemic_risk_id = models.ManyToManyField(Business_Systemic_Risk)
    business_structural_risk_id = models.ManyToManyField(
        Business_Structural_Risk)
    business_conditional_risk_id = models.ManyToManyField(
        Business_Conditional_Risk)
    business_condition_id = models.ManyToManyField(Business_Condition)
    business_preference_id = models.ManyToManyField(Business_Preference)
    business_finance_id = models.ManyToManyField(Business_Finance)
    business_risk_assessment = models.ForeignKey(Business_Risk_Assesment, on_delete=models.CASCADE, default=None)
    business_entity_id = models.ForeignKey(Business_Entity, on_delete=models.CASCADE, default=None)
