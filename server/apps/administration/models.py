from django.db import models


class Org_Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Org_Entity"


class Client_Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    authorization_type_code = models.CharField(max_length=32)
    authorization_entity = models.CharField(max_length=32)
    client_status_type_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Client_Entity"


class User_Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    client_entity_id = models.ForeignKey(to=Client_Entity, on_delete=models.CASCADE)
    org_entity_id = models.ForeignKey(to=Org_Entity, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=32)
    user_status_type_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "User_Entity"


class Auth_Level(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    row1 = models.IntegerField()
    row2 = models.IntegerField()
    row3 = models.IntegerField()

    class Meta:
        verbose_name_plural = "Auth_Level"


class User_Event(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "User_Event"


class Task_Entity(models.Model):
    id = models.IntegerField(primary_key=True)
    user_event_id = models.ForeignKey(to=User_Event, on_delete=models.CASCADE)
    native_id = models.IntegerField()
    status = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Task_Entity"


class Data_Set_Task_Entity(models.Model):
    class Meta:
        verbose_name_plural = "Data_Set_Task_Entity"


class Org_Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Org_Detail"


class Client_Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    client_entity_id = models.ForeignKey(to=Client_Entity, on_delete=models.CASCADE)
    org_detail_id = models.ForeignKey(to=Org_Detail, on_delete=models.CASCADE)
    industry = models.CharField(max_length=32)
    sector = models.CharField(max_length=32)
    annual_revenue = models.FloatField()
    annual_profit = models.FloatField()
    number_of_staff = models.IntegerField()

    class Meta:
        verbose_name_plural = "Client_Profile"
