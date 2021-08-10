from django.urls import path

from .views import (BalanceSheetView, BusinessBasicView, BusinessConditionView, BusinessFinanceView,
                    BusinessPreferenceView, CashflowView, IncomeStatementView)

app_name = "business"

cashflow_list = CashflowView.as_view({
    'post': 'post',
    'get': 'get'
})

cashflow_csv = CashflowView.as_view({
    'post': 'import_csv',
})

cashflow_detail = CashflowView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

balance_sheet_list = BalanceSheetView.as_view({
    'post': 'post',
    'get': 'get'
})

balance_sheet_csv = BalanceSheetView.as_view({
    'post': 'import_csv',
})

balance_sheet_detail = BalanceSheetView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('business_basic/', BusinessBasicView.as_view(), name="business_basic"),
    path('business_condition/', BusinessConditionView.as_view(),
         name="business_condition"),
    path('business_finance/', BusinessFinanceView.as_view(),
         name="business_finance"),
    path('business_preference/', BusinessPreferenceView.as_view(),
         name="business_preference"),
    path('income_statement/', IncomeStatementView.as_view(),
         name="income_statement"),
    path('business_cashflow/', cashflow_list, name="business_cashflow_list"),
    path('business_cashflow/<int:pk>/', cashflow_detail,
         name="business_cashflow_detail"),
    # path('business_cashflow/csv/', cashflow_csv, name="business_cashflow_csv"),
    path('balance_sheet/', balance_sheet_list, name="balance_sheet_list"),
    path('balance_sheet/<int:pk>/', balance_sheet_detail,
         name="balance_sheet_detail"),
    # path('balance_sheet/csv/', balance_sheet_csv, name="balance_sheet_csv"),
]
