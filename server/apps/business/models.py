from django.db import models
from apps.administration.models import Client_Entity, Org_Entity


class Business_Entity(models.Model):
    client_id = models.ForeignKey(Client_Entity, on_delete=models.CASCADE, default=None)
    org_id = models.ForeignKey(Org_Entity, on_delete=models.CASCADE, default=None)


class Business_Basic_Info(models.Model):
    # org_entity_id = ...
    business_name = models.CharField(max_length=30, blank=True, default="")
    address_1 = models.CharField(max_length=30, blank=True, default="")
    address_2 = models.CharField(max_length=30, blank=True, default="")
    city = models.CharField(max_length=30, blank=True, default="")
    state = models.CharField(max_length=30, blank=True, default="")
    zipcode = models.CharField(max_length=30, blank=True, default="")
    phone_number = models.CharField(max_length=30, blank=True, default="")
    email = models.CharField(max_length=30, blank=True, default="")
    sector = models.JSONField(blank=True, null=True)
    industry = models.CharField(max_length=30, blank=True, default="")
    website = models.CharField(max_length=30, blank=True, default="")
    number_of_employees = models.IntegerField(blank=True, default=1)
    description_of_business = models.CharField(
        max_length=50, blank=True, default="")

    # foreign key area.
    pass


class Business_Condition(models.Model):
    # own variables area.
    company_formation = models.CharField(max_length=50, blank=True, default="")
    business_model = models.CharField(max_length=50, blank=True, default="")
    leverage_on_tech = models.IntegerField(blank=True, default=0)
    competitiveness_1 = models.CharField(max_length=50, blank=True, default="")
    competitiveness_2 = models.CharField(max_length=50, blank=True, default="")
    competitiveness_3 = models.CharField(max_length=50, blank=True, default="")
    growth_1 = models.IntegerField(blank=True, default=0)
    growth_2 = models.IntegerField(blank=True, default=0)
    growth_3 = models.IntegerField(blank=True, default=0)
    top_risk_1 = models.CharField(max_length=50, blank=True, default="")
    top_risk_2 = models.CharField(max_length=50, blank=True, default="")
    top_risk_3 = models.CharField(max_length=50, blank=True, default="")
    rival_sector = models.CharField(max_length=50, blank=True, default="")
    competitor_1 = models.CharField(max_length=50, blank=True, default="")
    competitor_2 = models.CharField(max_length=50, blank=True, default="")
    competitor_3 = models.CharField(max_length=50, blank=True, default="")
    supplychain_risk = models.CharField(max_length=50, blank=True, default="")

    # foreign key area.
    business_basic_info = models.OneToOneField(
        Business_Basic_Info, on_delete=models.CASCADE, default=None, null=True)


class Cashflow(models.Model):
    # own variable area.
    year = models.IntegerField(blank=True, default=0)
    operating_cash_flow = models.CharField(
        max_length=50, blank=True, default="")
    cash_flow_from_continuing_operating_activities = models.CharField(
        max_length=50, blank=True, default="")
    net_income_from_continuing_operations = models.CharField(
        max_length=50, blank=True, default="")
    operating_gains_losses = models.CharField(
        max_length=50, blank=True, default="")
    depreciation_amortization_depletion = models.CharField(
        max_length=50, blank=True, default="")
    depreciation_and_amortization = models.CharField(
        max_length=50, blank=True, default="")
    deferred_tax = models.CharField(max_length=50, blank=True, default="")
    deferred_income_tax = models.CharField(
        max_length=50, blank=True, default="")
    provision_and_write_off_of_assets = models.CharField(
        max_length=50, blank=True, default="")
    stock_based_compensation = models.CharField(
        max_length=50, blank=True, default="")
    excess_tax_benefit_from_stock_based_compensation = models.CharField(
        max_length=50, blank=True, default="")
    other_non_cash_items = models.CharField(
        max_length=50, blank=True, default="")
    change_in_working_capital = models.CharField(
        max_length=50, blank=True, default="")
    change_in_receivables = models.CharField(
        max_length=50, blank=True, default="")
    change_in_account_receivables = models.CharField(
        max_length=50, blank=True, default="")
    change_in_inventory = models.CharField(
        max_length=50, blank=True, default="")
    change_in_payables_and_accrued_expense = models.CharField(
        max_length=50, blank=True, default="")
    change_in_other_current_liabilities = models.CharField(
        max_length=50, blank=True, default="")
    change_in_other_working_capital = models.CharField(
        max_length=50, blank=True, default="")
    investing_cash_flow = models.CharField(
        max_length=50, blank=True, default="")
    cash_flow_from_continuing_investing_activities = models.CharField(
        max_length=50, blank=True, default="")
    capital_expenditure_reported = models.CharField(
        max_length=50, blank=True, default="")
    net_business_purchase_and_sale = models.CharField(
        max_length=50, blank=True, default="")
    purchase_of_business = models.CharField(
        max_length=50, blank=True, default="")
    net_investment_purchase_and_sale = models.CharField(
        max_length=50, blank=True, default="")
    purchase_of_investment = models.CharField(
        max_length=50, blank=True, default="")
    sale_of_investment = models.CharField(
        max_length=50, blank=True, default="")
    net_other_investing_changes = models.CharField(
        max_length=50, blank=True, default="")
    financing_cash_flow = models.CharField(
        max_length=50, blank=True, default="")
    cash_flow_from_continuing_financing_activities = models.CharField(
        max_length=50, blank=True, default="")
    net_issuance_payments_of_debt = models.CharField(
        max_length=50, blank=True, default="")
    net_long_term_debt_issuance = models.CharField(
        max_length=50, blank=True, default="")
    long_term_debt_issuance = models.CharField(
        max_length=50, blank=True, default="")
    long_term_debt_payments = models.CharField(
        max_length=50, blank=True, default="")
    net_common_stock_issuance = models.CharField(
        max_length=50, blank=True, default="")
    common_stock_payments = models.CharField(
        max_length=50, blank=True, default="")
    cash_dividends_paid = models.CharField(
        max_length=50, blank=True, default="")
    common_stock_dividened_paid = models.CharField(
        max_length=50, blank=True, default="")
    proceeds_from_stock_option_exercised = models.CharField(
        max_length=50, blank=True, default="")
    net_other_financing_charges = models.CharField(
        max_length=50, blank=True, default="")
    end_cash_position = models.CharField(max_length=50, blank=True, default="")
    changes_in_cash = models.CharField(max_length=50, blank=True, default="")
    effect_of_exchange_rate_changes = models.CharField(
        max_length=50, blank=True, default="")
    beginning_cash_position = models.CharField(
        max_length=50, blank=True, default="")
    other_cash_adjustment_outside_change_in_cash = models.CharField(
        max_length=50, blank=True, default="")
    capital_expenditure = models.CharField(
        max_length=50, blank=True, default="")
    issuance_of_debt = models.CharField(max_length=50, blank=True, default="")
    repayment_of_debt = models.CharField(max_length=50, blank=True, default="")
    repurchase_of_capital_Stock = models.CharField(
        max_length=50, blank=True, default="")
    free_cash_flow = models.CharField(max_length=50, blank=True, default="")

    # foreign key area.
    pass


class Balance_sheet(models.Model):
    # own variable area.
    year = models.IntegerField(blank=True, default=0)
    total_assets = models.CharField(max_length=50, blank=True, default="")
    current_assets = models.CharField(max_length=50, blank=True, default="")
    cash_equivalents_and_short_term_investments = models.CharField(
        max_length=50, blank=True, default="")
    cash_and_cash_equivalents = models.CharField(
        max_length=50, blank=True, default="")
    receivables = models.CharField(max_length=50, blank=True, default="")
    accounts_receivable = models.CharField(
        max_length=50, blank=True, default="")
    gross_accounts_receivable = models.CharField(
        max_length=50, blank=True, default="")
    allowance_for_doubtful_accounts_receivable = models.CharField(
        max_length=50, blank=True, default="")
    inventory = models.CharField(max_length=50, blank=True, default="")
    raw_materials = models.CharField(max_length=50, blank=True, default="")
    finished_goods = models.CharField(max_length=50, blank=True, default="")
    other_inventories = models.CharField(max_length=50, blank=True, default="")
    prepaid_assets = models.CharField(max_length=50, blank=True, default="")
    restricted_cash = models.CharField(max_length=50, blank=True, default="")
    other_current_assets = models.CharField(
        max_length=50, blank=True, default="")
    total_non_current_assets = models.CharField(
        max_length=50, blank=True, default="")
    net_ppe = models.CharField(max_length=50, blank=True, default="")
    gross_ppe = models.CharField(max_length=50, blank=True, default="")
    properties = models.CharField(max_length=50, blank=True, default="")
    land_and_improvements = models.CharField(
        max_length=50, blank=True, default="")
    machinery_furniture_equipment = models.CharField(
        max_length=50, blank=True, default="")
    other_properties = models.CharField(max_length=50, blank=True, default="")
    construction_in_progress = models.CharField(
        max_length=50, blank=True, default="")
    leases = models.CharField(max_length=50, blank=True, default="")
    accumulated_depreciation = models.CharField(
        max_length=50, blank=True, default="")
    goodwill_and_other_intangible_assets = models.CharField(
        max_length=50, blank=True, default="")
    goodwill = models.CharField(max_length=50, blank=True, default="")
    other_intangible_assets = models.CharField(
        max_length=50, blank=True, default="")
    investments_and_advances = models.CharField(
        max_length=50, blank=True, default="")
    investment_in_financial_assets = models.CharField(
        max_length=50, blank=True, default="")
    trading_securities = models.CharField(
        max_length=50, blank=True, default="")
    non_current_deferred_assets = models.CharField(
        max_length=50, blank=True, default="")
    non_current_deffered_taxes_assets = models.CharField(
        max_length=50, blank=True, default="")
    other_non_current_assets = models.CharField(
        max_length=50, blank=True, default="")
    total_liabilities_net_minority_interest = models.CharField(
        max_length=50, blank=True, default="")
    current_liabilities = models.CharField(
        max_length=50, blank=True, default="")
    payables_and_accrued_expenses = models.CharField(
        max_length=50, blank=True, default="")
    payables = models.CharField(max_length=50, blank=True, default="")
    accounts_payable = models.CharField(max_length=50, blank=True, default="")
    current_accured_expenses = models.CharField(
        max_length=50, blank=True, default="")
    interest_payable = models.CharField(max_length=50, blank=True, default="")
    current_provisions = models.CharField(
        max_length=50, blank=True, default="")
    pesion_and_other_post_retirement_benefit_plans_current = models.CharField(
        max_length=50, blank=True, default="")
    current_debt_and_capital_lease_obligation = models.CharField(
        max_length=50, blank=True, default="")
    current_debt = models.CharField(max_length=50, blank=True, default="")
    other_current_borrowings = models.CharField(
        max_length=50, blank=True, default="")
    current_capital_lease_obligation = models.CharField(
        max_length=50, blank=True, default="")
    other_current_liabilities = models.CharField(
        max_length=50, blank=True, default="")
    total_non_current_liabilities_net_minority_interest = models.CharField(
        max_length=50, blank=True, default="")
    long_term_provisions = models.CharField(
        max_length=50, blank=True, default="")
    long_term_debt_and_capital_lease_obligation = models.CharField(
        max_length=50, blank=True, default="")
    long_term_debt = models.CharField(max_length=50, blank=True, default="")
    long_term_capital_lease_obligation = models.CharField(
        max_length=50, blank=True, default="")
    non_current_deferred_liabilities = models.CharField(
        max_length=50, blank=True, default="")
    non_current_deferred_taxes_liabilities = models.CharField(
        max_length=50, blank=True, default="")
    non_current_accrued_expenses = models.CharField(
        max_length=50, blank=True, default="")
    total_equity_gross_minority_interest = models.CharField(
        max_length=50, blank=True, default="")
    stockholders_equity = models.CharField(
        max_length=50, blank=True, default="")
    capital_stock = models.CharField(max_length=50, blank=True, default="")
    preferred_stock = models.CharField(max_length=50, blank=True, default="")
    common_stock = models.CharField(max_length=50, blank=True, default="")
    additional_paid_in_capital = models.CharField(
        max_length=50, blank=True, default="")
    retained_earnings = models.CharField(max_length=50, blank=True, default="")
    gains_losses_not_affecting_retained_earnings = models.CharField(
        max_length=50, blank=True, default="")
    total_capitalization = models.CharField(
        max_length=50, blank=True, default="")
    common_stock_equity = models.CharField(
        max_length=50, blank=True, default="")
    capital_lease_obligations = models.CharField(
        max_length=50, blank=True, default="")
    net_tangible_assets = models.CharField(
        max_length=50, blank=True, default="")
    working_capital = models.CharField(max_length=50, blank=True, default="")
    invested_capital = models.CharField(max_length=50, blank=True, default="")
    tangible_book_value = models.CharField(
        max_length=50, blank=True, default="")
    total_debt = models.CharField(max_length=50, blank=True, default="")
    net_debt = models.CharField(max_length=50, blank=True, default="")
    share_issued = models.CharField(max_length=50, blank=True, default="")
    ordinary_shares_number = models.CharField(
        max_length=50, blank=True, default="")

    # foreign key area.
    pass


class Income_Statement(models.Model):
    # own variable area.
    year = models.IntegerField(blank=True, default=0)
    total_revenue = models.CharField(max_length=50, blank=True, default="")
    operating_revenue = models.CharField(max_length=50, blank=True, default="")
    cost_of_revenue = models.CharField(max_length=50, blank=True, default="")
    gross_profit = models.CharField(max_length=50, blank=True, default="")
    operating_expense = models.CharField(max_length=50, blank=True, default="")
    selling_general_and_administrative = models.CharField(
        max_length=50, blank=True, default="")
    general_and_administrative_expense = models.CharField(
        max_length=50, blank=True, default="")
    other_g_and_a = models.CharField(max_length=50, blank=True, default="")
    selling_and_marketing_expense = models.CharField(
        max_length=50, blank=True, default="")
    operating_income = models.CharField(max_length=50, blank=True, default="")
    net_non_operating_interest_income_expense = models.CharField(
        max_length=50, blank=True, default="")
    interest_income_non_operating = models.CharField(
        max_length=50, blank=True, default="")
    interest_expense_non_operating = models.CharField(
        max_length=50, blank=True, default="")
    pretax_income = models.CharField(max_length=50, blank=True, default="")
    net_income_common_stockholders = models.CharField(
        max_length=50, blank=True, default="")
    net_income = models.CharField(max_length=50, blank=True, default="")
    net_income_including_non_controlling_interests = models.CharField(
        max_length=50, blank=True, default="")
    net_income_continuous_operations = models.CharField(
        max_length=50, blank=True, default="")
    diluted_ni_available_to_com_stockholders = models.CharField(
        max_length=50, blank=True, default="")
    basic_eps = models.CharField(max_length=50, blank=True, default="")
    diluted_eps = models.CharField(max_length=50, blank=True, default="")
    basic_average_shares = models.CharField(
        max_length=50, blank=True, default="")
    diluted_average_shares = models.CharField(
        max_length=50, blank=True, default="")
    total_operating_income_as_reported = models.CharField(
        max_length=50, blank=True, default="")
    total_expenses = models.CharField(max_length=50, blank=True, default="")
    net_income_from_continuing_and_discontinued_opertaions = models.CharField(
        max_length=50, blank=True, default="")
    normalized_income = models.CharField(max_length=50, blank=True, default="")
    interest_income = models.CharField(max_length=50, blank=True, default="")
    interest_expense = models.CharField(max_length=50, blank=True, default="")
    net_interest_income = models.CharField(
        max_length=50, blank=True, default="")
    ebit = models.CharField(max_length=50, blank=True, default="")
    ebitda = models.CharField(max_length=50, blank=True, default="")
    reconciled_cost_of_revenue = models.CharField(
        max_length=50, blank=True, default="")
    reconciled_depreciation = models.CharField(
        max_length=50, blank=True, default="")
    net_income_from_continuing_operation_net_minority_interest = models.CharField(
        max_length=50, blank=True, default="")
    normalized_ebitda = models.CharField(max_length=50, blank=True, default="")
    tax_rate_for_calcs = models.CharField(
        max_length=50, blank=True, default="")
    tax_effect_of_unusual_items = models.CharField(
        max_length=50, blank=True, default="")

    # foreign key area.
    pass


class Business_Finance(models.Model):
    # own variable area.
    annual_gross_revenue = models.CharField(max_length=50)
    annual_gross_profit = models.CharField(max_length=50)
    cash_ratio = models.CharField(max_length=50)
    quick_ratio = models.CharField(max_length=50)
    cash_position = models.CharField(max_length=50)
    annual_free_cashflow = models.CharField(max_length=50)
    total_debt = models.CharField(max_length=50)
    month_of_fiscal_year_end = models.CharField(max_length=50)
    total_business_worth = models.CharField(max_length=50)

    # foreign key area.
    business_basic_info = models.ForeignKey(
        Business_Basic_Info, on_delete=models.CASCADE, default=None)
    cashflow_2021 = models.ForeignKey(
        Cashflow, on_delete=models.CASCADE, related_name='cashflow_2021', default=None)
    balance_sheet_2021 = models.ForeignKey(
        Balance_sheet, on_delete=models.CASCADE, related_name='balancesheet_2021', default=None)
    income_statement_2021 = models.ForeignKey(
        Income_Statement, on_delete=models.CASCADE, related_name='incomestatement_2021', default=None)
    cashflow_2020 = models.ForeignKey(
        Cashflow, on_delete=models.CASCADE, related_name='cashflow_2020', default=None, null=True)
    balance_sheet_2020 = models.ForeignKey(
        Balance_sheet, on_delete=models.CASCADE, related_name='balancesheet_2020', default=None, null=True)
    income_statement_2020 = models.ForeignKey(
        Income_Statement, on_delete=models.CASCADE, related_name='incomestatement_2020', default=None, null=True)
    cashflow_2019 = models.ForeignKey(
        Cashflow, on_delete=models.CASCADE, related_name='cashflow_2019', default=None, null=True)
    balance_sheet_2019 = models.ForeignKey(
        Balance_sheet, on_delete=models.CASCADE, related_name='balancesheet_2019', default=None, null=True)
    income_statement_2019 = models.ForeignKey(
        Income_Statement, on_delete=models.CASCADE, related_name='incomestatement_2019', default=None, null=True)


class Business_Preference(models.Model):
    # own variable area.
    risk_tolerance = models.CharField(max_length=50, blank=True, default="")
    expected_duration = models.CharField(max_length=50, blank=True, default="")
    investor_type = models.CharField(max_length=50, blank=True, default="")
    preferred_sector_1 = models.IntegerField(blank=True, default=0)
    preferred_sector_2 = models.IntegerField(blank=True, default=0)
    preferred_sector_3 = models.IntegerField(blank=True, default=0)
    target_cash_balance = models.IntegerField(blank=True, default=0)
    disliked_asset_class_1 = models.IntegerField(blank=True, default=0)
    disliked_asset_class_2 = models.IntegerField(blank=True, default=0)
    disliked_asset_class_3 = models.IntegerField(blank=True, default=0)
    interested_asset_class_1 = models.IntegerField(blank=True, default=0)
    interested_asset_class_2 = models.IntegerField(blank=True, default=0)
    interested_asset_class_3 = models.IntegerField(blank=True, default=0)
    country_refused_1 = models.CharField(max_length=50, blank=True, default='')
    country_refused_2 = models.CharField(max_length=50, blank=True, default='')
    country_refused_3 = models.CharField(max_length=50, blank=True, default='')
    country_interested_1 = models.CharField(
        max_length=50, blank=True, default='')
    country_interested_2 = models.CharField(
        max_length=50, blank=True, default='')
    country_interested_3 = models.CharField(
        max_length=50, blank=True, default='')
    projected_major_spending = models.CharField(
        max_length=50, blank=True, default='')
    projected_spending_amt = models.IntegerField(blank=True, default=0)
    cash_set_aside = models.IntegerField(blank=True, default=0)
    _100k_1m_50percent = models.CharField(
        max_length=50, blank=True, default='')
    _100k_500k_50percen = models.CharField(
        max_length=50, blank=True, default='')
    _100k_1m_30percent = models.CharField(
        max_length=50, blank=True, default='')
    how_often_availability = models.CharField(
        max_length=50, blank=True, default='')

    # foreign key area.
    business_basic_info = models.OneToOneField(
        Business_Basic_Info, on_delete=models.CASCADE)
