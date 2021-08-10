from django.urls import path

from .views import (NasdaqView, auto_complete, market_auto_complete,
                    get_market_earnings, get_market_movers, get_market_quotes, get_market_spark,
                    get_market_summary, get_market_trending_tickers, get_sp500_data, get_stock_analysis,
                    get_stock_balance_sheet, get_stock_cash_flow, get_stock_detail, get_stock_financials,
                    get_stock_historical_data, get_stock_holders, get_stock_insider_roster,
                    get_stock_insider_transactions, get_stock_profile, get_stock_recommendation, get_stock_statistics,
                    get_stock_summary, get_stock_upgrades_downgrades, get_yahoo_data)

app_name = "market"

nasdaq_list = NasdaqView.as_view({
    'post': 'post',
    'get': 'get',
})

nasdaq_csv = NasdaqView.as_view({
    'post': 'import_csv',
})

urlpatterns = [

    path('yahoo/auto-complete/', auto_complete, name="yahoo_auto_complete"),
    # Yahoo Stock
    path('yahoo/stock/get-summary/', get_stock_summary, name="yahoo_stock_summary"),
    path('yahoo/stock/get-recommendation/', get_stock_recommendation, name="yahoo_stock_recommendation"),
    path('yahoo/stock/get-upgrades-downgrades/', get_stock_upgrades_downgrades, name="stock_upgrades_downgrades"),
    # Chart may not be needed, keep as place nolder
    # path('yahoo/stock/get-chart/', get_stock_chart, name="stock_chart"),
    path('yahoo/stock/get-statistics/', get_stock_statistics, name="yahoo_stock_statistics"),
    path('yahoo/stock/get-historical-data/', get_stock_historical_data, name="yahoo_stock_historical_data"),
    path('yahoo/stock/get-profile/', get_stock_profile, name="yahoo_stock_profile"),
    path('yahoo/stock/get-financials/', get_stock_financials, name="yahoo_stock_financials"),
    path('yahoo/stock/get-cash-flow/', get_stock_cash_flow, name="yahoo_stock_cashflow"),
    path('yahoo/stock/get-balance-sheet/', get_stock_balance_sheet, name="yahoo_stock_balance_sheet"),
    path('yahoo/stock/get-analysis/', get_stock_analysis, name="yahoo_stock_analysis"),
    # Options may not be needed, keep as placeholder
    # path('yahoo/stock/get-options/', get_stock_options, name="yahoo_stock_options"),
    path('yahoo/stock/get-holders/', get_stock_holders, name="yahoo_stock_holders"),
    path(
        'yahoo/stock/get-insider-transactions/',
        get_stock_insider_transactions,
        name="yahoo_stock_insider_transactions",
    ),
    path('yahoo/stock/get-insider-roster/', get_stock_insider_roster, name="yahoo_stock_insider_roster"),
    path('yahoo/stock/get-detail/', get_stock_detail, name="yahoo_stock_detail"),
    # Get Histories may not be needed, keep as placeholder
    # path('yahoo/stock/get-histories/', get_stock_histories,  name="yahoo_stock_histories"),

    # Yahoo Market
    path('yahoo/market/get-quotes/', get_market_quotes, name="yahoo_market_quotes"),
    path('yahoo/market/get-movers/', get_market_movers, name="yahoo_market_movers"),
    path('yahoo/market/get-summary/', get_market_summary, name="yahoo_market_summary"),
    path('yahoo/market/get-spark/', get_market_spark, name="yahoo_market_spark"),
    path('yahoo/market/get-earnings/', get_market_earnings, name="yahoo_market_earnings"),
    path('yahoo/market/get-trending-tickers/', get_market_trending_tickers, name="yahoo_market_trending_tickers"),
    path('yahoo/market/auto-complete/', market_auto_complete, name="yahoo_market_auto_complete"),

    # NZJ code-----------------------------------------------
    # path('yahoo/nasdaq', YahooView.as_view(), name="yahoo"),
    path('yahoo/data/', get_yahoo_data, name="yahoo_data"),
    path('sp500/', get_sp500_data, name="sp500"),
    path('tickers/nasdaq/', nasdaq_list, name="tickers_nasdaq"),
    path('tickers/nasdaq/csv/', nasdaq_csv, name="tickers_nasdaq_csv"),
]
