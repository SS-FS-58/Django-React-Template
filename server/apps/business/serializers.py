from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (Balance_sheet, Business_Basic_Info, Business_Condition, Business_Finance, Business_Preference,
                     Cashflow, Income_Statement)


class BusinessBasicSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(required=False)
    address_1 = serializers.CharField(required=False)
    address_2 = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    zipcode = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    sector = serializers.JSONField(required=False)
    industry = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    number_of_employees = serializers.IntegerField(required=False)
    description_of_business = serializers.CharField(required=False)

    class Meta:
        model = Business_Basic_Info
        fields = '__all__'


class BusinessConditionSerializer(serializers.ModelSerializer):
    company_formation = serializers.CharField(required=False)
    business_model = serializers.CharField(required=False)
    leverage_on_tech = serializers.IntegerField(required=False)
    competitiveness_1 = serializers.CharField(required=False)
    competitiveness_2 = serializers.CharField(required=False)
    competitiveness_3 = serializers.CharField(required=False)
    growth_1 = serializers.IntegerField(required=False)
    growth_2 = serializers.IntegerField(required=False)
    growth_3 = serializers.IntegerField(required=False)
    top_risk_1 = serializers.CharField(required=False)
    top_risk_2 = serializers.CharField(required=False)
    top_risk_3 = serializers.CharField(required=False)
    rival_sector = serializers.CharField(required=False)
    competitor_1 = serializers.CharField(required=False)
    competitor_2 = serializers.CharField(required=False)
    competitor_3 = serializers.CharField(required=False)
    supplychain_risk = serializers.CharField(required=False)
    business_basic_info_id = serializers.IntegerField(required=False)

    class Meta:
        model = Business_Condition
        exclude = ("business_basic_info",)

    def validate(self, data):
        # Validate if business basic info is exist with requested id
        if not Business_Basic_Info.objects.filter(
                pk=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info not exist with ID="+str(data["business_basic_info_id"]))
        # Validate if business basic info is already associated with requested id
        if Business_Condition.objects.filter(business_basic_info=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info ID="+str(data["business_basic_info_id"]) + " already associated")
        return data

    def create(self, validated_data):
        # Get business basic info from business basic info id & set as FK
        basic_info = Business_Basic_Info.objects.filter(
            pk=validated_data["business_basic_info_id"]).first()
        bcs = Business_Condition(
            business_basic_info=basic_info, **validated_data)
        bcs.save()
        return bcs


class BusinessPreferenceSerializer(serializers.ModelSerializer):
    # own variable area.
    risk_tolerance = serializers.CharField(required=True)
    expected_duration = serializers.CharField(required=True)
    investor_type = serializers.CharField(required=False)
    preferred_sector_1 = serializers.IntegerField(required=True)
    preferred_sector_2 = serializers.IntegerField(required=False)
    preferred_sector_3 = serializers.IntegerField(required=False)
    target_cash_balance = serializers.IntegerField(required=False)
    disliked_asset_class_1 = serializers.IntegerField(required=False)
    disliked_asset_class_2 = serializers.IntegerField(required=False)
    disliked_asset_class_3 = serializers.IntegerField(required=False)
    interested_asset_class_1 = serializers.IntegerField(required=False)
    interested_asset_class_2 = serializers.IntegerField(required=False)
    interested_asset_class_3 = serializers.IntegerField(required=False)
    country_refused_1 = serializers.CharField(required=False)
    country_refused_2 = serializers.CharField(required=False)
    country_refused_3 = serializers.CharField(required=False)
    country_interested_1 = serializers.CharField(required=False)
    country_interested_2 = serializers.CharField(required=False)
    country_interested_3 = serializers.CharField(required=False)
    projected_major_spending = serializers.CharField(required=True)
    projected_spending_amt = serializers.CharField(required=True)
    cash_set_aside = serializers.IntegerField(required=True)
    _100k_1m_50percent = serializers.IntegerField(required=True)
    _100k_500k_50percen = serializers.CharField(required=True)
    _100k_1m_30percent = serializers.CharField(required=True)
    how_often_availability = serializers.CharField(required=True)
    business_basic_info_id = serializers.IntegerField(required=True)

    class Meta:
        model = Business_Preference
        exclude = ("business_basic_info",)

    def validate(self, data):
        # Validate if business basic info is exist with requested id
        if not Business_Basic_Info.objects.filter(
                pk=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info not exist with ID="+str(data["business_basic_info_id"]))
        # Validate if business basic info is already associated with requested id
        if Business_Preference.objects.filter(business_basic_info=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info ID="+str(data["business_basic_info_id"]) + " already associated")
        return data

    def create(self, validated_data):
        # Get business basic info from business basic info id & set as FK
        basic_info = Business_Basic_Info.objects.filter(
            pk=validated_data["business_basic_info_id"]).first()
        bps = Business_Preference(
            business_basic_info=basic_info, **validated_data)
        bps.save()
        return bps


class BusinessFinanceSerializer(serializers.ModelSerializer):
    # own variable area.
    annual_gross_revenue = serializers.CharField(required=True)
    annual_gross_profit = serializers.CharField(required=True)
    cash_ratio = serializers.CharField(required=True)
    quick_ratio = serializers.CharField(required=True)
    cash_position = serializers.CharField(required=True)
    annual_free_cashflow = serializers.CharField(required=True)
    total_debt = serializers.CharField(required=True)
    month_of_fiscal_year_end = serializers.CharField(required=True)
    total_business_worth = serializers.CharField(required=True)
    business_basic_info_id = serializers.IntegerField(required=True)
    cashflow_2021_id = serializers.IntegerField(required=True)
    balance_sheet_2021_id = serializers.IntegerField(required=True)
    income_statement_2021_id = serializers.IntegerField(required=True)
    cashflow_2020_id = serializers.IntegerField(required=False)
    balance_sheet_2020_id = serializers.IntegerField(required=False)
    income_statement_2020_id = serializers.IntegerField(required=False)
    cashflow_2019_id = serializers.IntegerField(required=False)
    balance_sheet_2019_id = serializers.IntegerField(required=False)
    income_statement_2019_id = serializers.IntegerField(required=False)

    class Meta:
        model = Business_Finance
        exclude = ("business_basic_info", 'cashflow_2021', 'cashflow_2020', 'cashflow_2019', 'balance_sheet_2021',
                   'balance_sheet_2020', 'balance_sheet_2019', 'income_statement_2021', 'income_statement_2020',
                   'income_statement_2019')

    def validate(self, data):
        # Validate if business basic info is exist with requested id
        if not Business_Basic_Info.objects.filter(
                pk=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info not exist with ID="+str(data["business_basic_info_id"]))
        # Validate if business basic info is already associated with requested id
        if Business_Finance.objects.filter(business_basic_info=data["business_basic_info_id"]).exists():
            raise ValidationError(
                "Business Info ID="+str(data["business_basic_info_id"]) + " already associated")
        return data

    def create(self, validated_data):
        # Get business basic info from business basic info id & set as FK
        basic_info = Business_Basic_Info.objects.filter(
            pk=validated_data["business_basic_info_id"]).first()

        # Get Cash Flow, Income Statement, BalanceSheet FK
        cashflow21 = Cashflow.objects.filter(
            pk=validated_data["cashflow_2021_id"]).first()
        income21 = Income_Statement.objects.filter(
            pk=validated_data["income_statement_2021_id"]).first()
        balance21 = Balance_sheet.objects.filter(
            pk=validated_data["balance_sheet_2021_id"]).first()
        cashflow20 = None
        cashflow19 = None
        income20 = None
        income19 = None
        balance20 = None
        balance19 = None
        if 'cashflow_2020_id' in validated_data:
            cashflow20 = Cashflow.objects.filter(
                pk=validated_data["cashflow_2020_id"]).first()
        if 'cashflow_2019_id' in validated_data:
            cashflow19 = Cashflow.objects.filter(
                pk=validated_data["cashflow_2019_id"]).first()
        if 'income_statement_2020_id' in validated_data:
            income20 = Income_Statement.objects.filter(
                pk=validated_data["income_statement_2020_id"]).first()
        if 'income_statement_2019_id' in validated_data:
            income19 = Income_Statement.objects.filter(
                pk=validated_data["income_statement_2019_id"]).first()
        if 'balance_sheet_2020_id' in validated_data:
            balance20 = Balance_sheet.objects.filter(
                pk=validated_data["balance_sheet_2020_id"]).first()
        if 'balance_sheet_2019_id' in validated_data:
            balance19 = Balance_sheet.objects.filter(
                pk=validated_data["balance_sheet_2019_id"]).first()

        bfs = Business_Finance(
            business_basic_info=basic_info, cashflow_2021=cashflow21, cashflow_2020=cashflow20,
            cashflow_2019=cashflow19, balance_sheet_2021=balance21, balance_sheet_2020=balance20,
            balance_sheet_2019=balance19, income_statement_2021=income21, income_statement_2020=income20,
            income_statement_2019=income19, **validated_data,
        )
        bfs.save()
        return bfs


class IncomeStatementSerializer(serializers.ModelSerializer):
    # own variable area.
    year = serializers.IntegerField(required=True)
    total_revenue = serializers.CharField(required=False)
    operating_revenue = serializers.CharField(required=False)
    cost_of_revenue = serializers.CharField(required=False)
    gross_profit = serializers.CharField(required=False)
    operating_expense = serializers.CharField(required=False)
    selling_general_and_administrative = serializers.CharField(required=False)
    general_and_administrative_expense = serializers.CharField(required=False)
    other_g_and_a = serializers.CharField(required=False)
    selling_and_marketing_expense = serializers.CharField(required=False)
    operating_income = serializers.CharField(required=False)
    net_non_operating_interest_income_expense = serializers.CharField(
        required=False)
    interest_income_non_operating = serializers.CharField(required=False)
    interest_expense_non_operating = serializers.CharField(required=False)
    pretax_income = serializers.CharField(required=False)
    net_income_common_stockholders = serializers.CharField(required=False)
    net_income = serializers.CharField(required=False)
    net_income_including_non_controlling_interests = serializers.CharField(
        required=False)
    net_income_continuous_operations = serializers.CharField(required=False)
    diluted_ni_available_to_com_stockholders = serializers.CharField(
        required=False)
    basic_eps = serializers.CharField(required=False)
    diluted_eps = serializers.CharField(required=False)
    basic_average_shares = serializers.CharField(required=False)
    diluted_average_shares = serializers.CharField(required=False)
    total_operating_income_as_reported = serializers.CharField(required=False)
    total_expenses = serializers.CharField(required=False)
    net_income_from_continuing_and_discontinued_opertaions = serializers.CharField(
        required=False)
    normalized_income = serializers.CharField(required=False)
    interest_income = serializers.CharField(required=False)
    interest_expense = serializers.CharField(required=False)
    net_interest_income = serializers.CharField(required=False)
    ebit = serializers.CharField(required=False)
    ebitda = serializers.CharField(required=False)
    reconciled_cost_of_revenue = serializers.CharField(required=False)
    reconciled_depreciation = serializers.CharField(required=False)
    net_income_from_continuing_operation_net_minority_interest = serializers.CharField(
        required=False)
    normalized_ebitda = serializers.CharField(required=False)
    tax_rate_for_calcs = serializers.CharField(required=False)
    tax_effect_of_unusual_items = serializers.CharField(required=False)

    class Meta:
        model = Income_Statement
        fields = "__all__"

        # exclude = ["business_basic_info_id"]


class CashflowSerializer(serializers.ModelSerializer):

    year = serializers.IntegerField(required=False)
    operating_cash_flow = serializers.CharField(required=False)
    cash_flow_from_continuing_operating_activities = serializers.CharField(
        required=False)
    net_income_from_continuing_operations = serializers.CharField(
        required=False)
    operating_gains_losses = serializers.CharField(required=False)
    depreciation_amortization_depletion = serializers.CharField(required=False)
    depreciation_and_amortization = serializers.CharField(required=False)
    deferred_tax = serializers.CharField(required=False)
    deferred_income_tax = serializers.CharField(required=False)
    provision_and_write_off_of_assets = serializers.CharField(required=False)
    stock_based_compensation = serializers.CharField(required=False)
    excess_tax_benefit_from_stock_based_compensation = serializers.CharField(
        required=False)
    other_non_cash_items = serializers.CharField(required=False)
    change_in_working_capital = serializers.CharField(required=False)
    change_in_receivables = serializers.CharField(required=False)
    change_in_account_receivables = serializers.CharField(required=False)
    change_in_inventory = serializers.CharField(required=False)
    change_in_payables_and_accrued_expense = serializers.CharField(
        required=False)
    change_in_other_current_liabilities = serializers.CharField(required=False)
    change_in_other_working_capital = serializers.CharField(required=False)
    investing_cash_flow = serializers.CharField(required=False)
    cash_flow_from_continuing_investing_activities = serializers.CharField(
        required=False)
    capital_expenditure_reported = serializers.CharField(required=False)
    net_business_purchase_and_sale = serializers.CharField(required=False)
    purchase_of_business = serializers.CharField(required=False)
    net_investment_purchase_and_sale = serializers.CharField(required=False)
    purchase_of_investment = serializers.CharField(required=False)
    sale_of_investment = serializers.CharField(required=False)
    net_other_investing_changes = serializers.CharField(required=False)
    financing_cash_flow = serializers.CharField(required=False)
    cash_flow_from_continuing_financing_activities = serializers.CharField(
        required=False)
    net_issuance_payments_of_debt = serializers.CharField(required=False)
    net_long_term_debt_issuance = serializers.CharField(required=False)
    long_term_debt_issuance = serializers.CharField(required=False)
    long_term_debt_payments = serializers.CharField(required=False)
    net_common_stock_issuance = serializers.CharField(required=False)
    common_stock_payments = serializers.CharField(required=False)
    cash_dividends_paid = serializers.CharField(required=False)
    common_stock_dividened_paid = serializers.CharField(required=False)
    proceeds_from_stock_option_exercised = serializers.CharField(
        required=False)
    net_other_financing_charges = serializers.CharField(required=False)
    end_cash_position = serializers.CharField(required=False)
    changes_in_cash = serializers.CharField(required=False)
    effect_of_exchange_rate_changes = serializers.CharField(required=False)
    beginning_cash_position = serializers.CharField(required=False)
    other_cash_adjustment_outside_change_in_cash = serializers.CharField(
        required=False)
    capital_expenditure = serializers.CharField(required=False)
    issuance_of_debt = serializers.CharField(required=False)
    repayment_of_debt = serializers.CharField(required=False)
    repurchase_of_capital_Stock = serializers.CharField(required=False)
    free_cash_flow = serializers.CharField(required=False)

    class Meta:
        model = Cashflow
        fields = '__all__'


class BalanceSheetSerializer(serializers.ModelSerializer):

    year = serializers.IntegerField(required=False)
    total_assets = serializers.CharField(required=False)
    current_assets = serializers.CharField(required=False)
    cash_equivalents_and_short_term_investments = serializers.CharField(
        required=False)
    cash_and_cash_equivalents = serializers.CharField(required=False)
    receivables = serializers.CharField(required=False)
    accounts_receivable = serializers.CharField(required=False)
    gross_accounts_receivable = serializers.CharField(required=False)
    allowance_for_doubtful_accounts_receivable = serializers.CharField(
        required=False)
    inventory = serializers.CharField(required=False)
    raw_materials = serializers.CharField(required=False)
    finished_goods = serializers.CharField(required=False)
    other_inventories = serializers.CharField(required=False)
    prepaid_assets = serializers.CharField(required=False)
    restricted_cash = serializers.CharField(required=False)
    other_current_assets = serializers.CharField(required=False)
    total_non_current_assets = serializers.CharField(required=False)
    net_ppe = serializers.CharField(required=False)
    gross_ppe = serializers.CharField(required=False)
    properties = serializers.CharField(required=False)
    land_and_improvements = serializers.CharField(required=False)
    machinery_furniture_equipment = serializers.CharField(required=False)
    other_properties = serializers.CharField(required=False)
    construction_in_progress = serializers.CharField(required=False)
    leases = serializers.CharField(required=False)
    accumulated_depreciation = serializers.CharField(required=False)
    goodwill_and_other_intangible_assets = serializers.CharField(
        required=False)
    goodwill = serializers.CharField(required=False)
    other_intangible_assets = serializers.CharField(required=False)
    investments_and_advances = serializers.CharField(required=False)
    investment_in_financial_assets = serializers.CharField(required=False)
    trading_securities = serializers.CharField(required=False)
    non_current_deferred_assets = serializers.CharField(required=False)
    non_current_deffered_taxes_assets = serializers.CharField(required=False)
    other_non_current_assets = serializers.CharField(required=False)
    total_liabilities_net_minority_interest = serializers.CharField(
        required=False)
    current_liabilities = serializers.CharField(required=False)
    payables_and_accrued_expenses = serializers.CharField(required=False)
    payables = serializers.CharField(required=False)
    accounts_payable = serializers.CharField(required=False)
    current_accured_expenses = serializers.CharField(required=False)
    interest_payable = serializers.CharField(required=False)
    current_provisions = serializers.CharField(required=False)
    pesion_and_other_post_retirement_benefit_plans_current = serializers.CharField(
        required=False)
    current_debt_and_capital_lease_obligation = serializers.CharField(
        required=False)
    current_debt = serializers.CharField(required=False)
    other_current_borrowings = serializers.CharField(required=False)
    current_capital_lease_obligation = serializers.CharField(required=False)
    other_current_liabilities = serializers.CharField(required=False)
    total_non_current_liabilities_net_minority_interest = serializers.CharField(
        required=False)
    long_term_provisions = serializers.CharField(required=False)
    long_term_debt_and_capital_lease_obligation = serializers.CharField(
        required=False)
    long_term_debt = serializers.CharField(required=False)
    long_term_capital_lease_obligation = serializers.CharField(required=False)
    non_current_deferred_liabilities = serializers.CharField(required=False)
    non_current_deferred_taxes_liabilities = serializers.CharField(
        required=False)
    non_current_accrued_expenses = serializers.CharField(required=False)
    total_equity_gross_minority_interest = serializers.CharField(
        required=False)
    stockholders_equity = serializers.CharField(required=False)
    capital_stock = serializers.CharField(required=False)
    preferred_stock = serializers.CharField(required=False)
    common_stock = serializers.CharField(required=False)
    additional_paid_in_capital = serializers.CharField(required=False)
    retained_earnings = serializers.CharField(required=False)
    gains_losses_not_affecting_retained_earnings = serializers.CharField(
        required=False)
    total_capitalization = serializers.CharField(required=False)
    common_stock_equity = serializers.CharField(required=False)
    capital_lease_obligations = serializers.CharField(required=False)
    net_tangible_assets = serializers.CharField(required=False)
    working_capital = serializers.CharField(required=False)
    invested_capital = serializers.CharField(required=False)
    tangible_book_value = serializers.CharField(required=False)
    total_debt = serializers.CharField(required=False)
    net_debt = serializers.CharField(required=False)
    share_issued = serializers.CharField(required=False)
    ordinary_shares_number = serializers.CharField(required=False)

    class Meta:
        model = Balance_sheet
        fields = '__all__'


class ImportCsvSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=True)
    csv = serializers.FileField(max_length=None, allow_empty_file=False)
