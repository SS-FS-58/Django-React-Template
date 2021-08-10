from django.db import models


class Nasdaq(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=200)
    company_security_name = models.CharField(max_length=200)

    # foreign key area.
    pass
