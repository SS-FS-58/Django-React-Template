from django.db import models

from apps.administration.models import Org_Entity, User_Entity


class User_Personal_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    user_entity_id = models.ForeignKey(
        to=User_Entity, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    suffix = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    division = models.CharField(max_length=32)
    employee_number = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "User_Personal_Info"


class Org_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=32)
    contact_number = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Org_Info"


class Plan_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    plan_type = models.CharField(max_length=32)
    plan_cost = models.FloatField()

    class Meta:
        verbose_name_plural = "Plan_Info"


class Org_Plan_Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    plan_info_id = models.ForeignKey(to=Plan_Info, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Org_Plan_Entity"


class Billing_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Billing_Info"


class Org_Account(models.Model):
    id = models.IntegerField(primary_key=True)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=32)
    number_of_users = models.IntegerField()

    class Meta:
        verbose_name_plural = "Org_Account"


class User_Account(models.Model):
    id = models.IntegerField(primary_key=True)
    org_account_id = models.ForeignKey(
        to=Org_Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "User_Account"


class User_Permission(models.Model):
    id = models.IntegerField(primary_key=True)
    create_super_user = models.BooleanField()
    change_plan = models.BooleanField()
    create_account_admin = models.BooleanField()
    create_account = models.BooleanField()
    manage_user = models.BooleanField()
    manage_project = models.BooleanField()

    class Meta:
        verbose_name_plural = "User_Permission"


class User_Language_Timezone(models.Model):
    id = models.IntegerField(primary_key=True)
    user_entity_id = models.ForeignKey(
        to=User_Entity, on_delete=models.CASCADE)
    time_zone = models.CharField(max_length=32, default="UTC")
    locale = models.CharField(max_length=32)
    language = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "User_Language_Timezone"
