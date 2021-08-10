from django.contrib import admin

from .models import (Balance_sheet, Business_Basic_Info, Business_Condition, Business_Finance, Business_Preference,
                     Cashflow, Income_Statement)

# Register your models here.
admin.site.register(Business_Basic_Info)
admin.site.register(Business_Condition)
admin.site.register(Cashflow)
admin.site.register(Balance_sheet)
admin.site.register(Income_Statement)
admin.site.register(Business_Finance)
admin.site.register(Business_Preference)
