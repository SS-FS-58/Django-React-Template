import pandas as pd
import requests
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from pandas import DataFrame
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from yahoo_fin.stock_info import get_data

from .models import Nasdaq
from .serializers import (ImportCsvSerializer, NasdaqSerializer, YahooDataRequestSerializer,
                          YahooAutoCompleteRequestSerializer, YahooMarketAutoCompleteRequest,
                          YahooDataResponseSerializer, YahooMarketEarningsRequest, YahooMarketMoversRequest,
                          YahooMarketQuotesRequest, YahooMarketSparkRequest, YahooRegionRequest,
                          YahooStockRequestSerializer, YahooSymbolRequest)

DAY_INTERVAL = '1d'
WEEK_INTERVAL = '1wk'
MONTH_INTERVAL = '1mo'

# Create your views here.
YAHOO_URL_V1 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"
YAHOO_STOCK_URL_V1 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/"
YAHOO_STOCK_URL_V2 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/"
YAHOO_MARKET_URL_V1 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/"
YAHOO_MARKET_URL_V2 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/"

# querystring = {"symbol":"AMRN","region":"US"}

YAHOO_API_HEADERS = {
    'x-rapidapi-key': "58567a0020msh29544832f1db6e6p1bb1bfjsn71974f8ad5e8",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
}


# YAHOO API STOCK ENDPOINTS NOT IMPLEMENTED. Are they needed?
# get-chart, get-timeseries, get-options

# Sample API parameters: q: "GOOG", region: "US"
@api_view(['POST'])
def auto_complete(request):
    auto_complete_path = "auto-complete"
    yahoo_endpoint = YAHOO_URL_V1 + auto_complete_path
    serializer_class = YahooAutoCompleteRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_summary(request):
    stock_summary_path = "get-summary"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_summary_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_recommendation(request):
    stock_recommendation_path = "get-recommendations"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_recommendation_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_upgrades_downgrades(request):
    stock_upgrades_downgrades_path = "get-upgrades-downgrades"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_upgrades_downgrades_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: interval":"5m","symbol":"AMRN", "range":"1d","region":"US"
@api_view(['POST'])
def get_stock_chart(request):
    pass


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_statistics(request):
    stock_statistics_path = "get-statistics"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_statistics_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_historical_data(request):
    stock_historical_data_path = "get-historical-data"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_historical_data_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_profile(request):
    stock_profile_path = "get-profile"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_profile_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_financials(request):
    stock_financials_path = "get-financials"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_financials_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "symbol":"IBM","period2":"1571590800","period1":"493578000","region":"US"
@api_view(['POST'])
def get_stock_timeseries(request):
    pass


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_cash_flow(request):
    stock_cash_flow_path = "get-cash-flow"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_cash_flow_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_balance_sheet(request):
    stock_balance_sheet_path = "get-balance-sheet"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_balance_sheet_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US"
@api_view(['POST'])
def get_stock_analysis(request):
    stock_analysis_path = "get-analysis"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_analysis_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "symbol":"AMRN","date":"1562284800", "region":"US"
@api_view(['POST'])
def get_stock_options(request):
    pass


# Sample API parameters: symbol: "GOOG", region: "US",
@api_view(['POST'])
def get_stock_holders(request):
    stock_holders_path = "get-holders"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_holders_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG"
@api_view(['POST'])
def get_stock_insights(request):
    stock_insights_path = "get-insights"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_insights_path
    serializer_class = YahooSymbolRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US",
@api_view(['POST'])
def get_stock_insider_transactions(request):
    stock_insider_transactions_path = "get-insider-transactions"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_insider_transactions_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US",
@api_view(['POST'])
def get_stock_insider_roster(request):
    stock_insider_roster_path = "get-insider-roster"
    yahoo_endpoint = YAHOO_STOCK_URL_V2 + stock_insider_roster_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: symbol: "GOOG", region: "US",
@api_view(['POST'])
def get_stock_detail(request):
    stock_detail_path = "get-detail"
    yahoo_endpoint = YAHOO_STOCK_URL_V1 + stock_detail_path
    serializer_class = YahooStockRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "symbol":"NBEV","from":"1546448400","to":"1562086800","events":"div","interval":"1d",
# "region":"US"
@api_view(['POST'])
def get_stock_histories(request):
    pass


# Sample API parameters: "region":"US","symbols":"AMD,IBM,AAPL"
@api_view(['POST'])
def get_market_quotes(request):
    market_qutoes_path = "get-quotes"
    yahoo_endpoint = YAHOO_MARKET_URL_V2 + market_qutoes_path
    serializer_class = YahooMarketQuotesRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "region":"US","lang":"en-US","count":"6","start":"0"
@api_view(['POST'])
def get_market_movers(request):
    market_movers_path = "get-movers"
    yahoo_endpoint = YAHOO_MARKET_URL_V2 + market_movers_path
    serializer_class = YahooMarketMoversRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "region":"US"
@api_view(['POST'])
def get_market_summary(request):
    market_summary_path = "get-summary"
    yahoo_endpoint = YAHOO_MARKET_URL_V2 + market_summary_path
    serializer_class = YahooRegionRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "symbol":"HYDR.ME","interval":"5m","range":"1d","region":"US","comparisons":"^GDAXI,^FCHI"
@api_view(['POST'])
def get_market_charts(request):
    pass


# Sample API parameters:"symbols":"AMZN,AAPL,WDC,REYN,AZN,YM=F","interval":"1m","range":"1d"
@api_view(['POST'])
def get_market_spark(request):
    market_spark_path = "get-spark"
    yahoo_endpoint = YAHOO_MARKET_URL_V1 + market_spark_path
    serializer_class = YahooMarketSparkRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "region":"US","startDate":"1585155600000","endDate":"1589475600000","size":"10"
@api_view(['POST'])
def get_market_earnings(request):
    market_earnings_path = "get-earnings"
    yahoo_endpoint = YAHOO_MARKET_URL_V1 + market_earnings_path
    serializer_class = YahooMarketEarningsRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: "region":"US"
@api_view(['POST'])
def get_market_trending_tickers(request):
    market_trending_tickers_path = "get-trending-tickers"
    yahoo_endpoint = YAHOO_MARKET_URL_V1 + market_trending_tickers_path
    serializer_class = YahooRegionRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# Sample API parameters: q: "GOOG", region: "US"
@api_view(['POST'])
def market_auto_complete(request):
    auto_complete_path = "auto-complete"
    yahoo_endpoint = YAHOO_MARKET_URL_V1 + auto_complete_path
    serializer_class = YahooMarketAutoCompleteRequest(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    response_data = {"success": True}

    try:
        response = requests.request("GET", yahoo_endpoint,
                                    headers=YAHOO_API_HEADERS, params=request.data)
        response_data["data"] = response.json()

    except AssertionError:
        response_data["data"] = []

    return Response(data=response_data, status=status.HTTP_200_OK)


# nzj code------------------------------------------------------------------
@api_view(['POST'])
def get_yahoo_data(request):
    serializer_class = YahooDataRequestSerializer(data=request.data)

    if not serializer_class.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    company = request.data.get('company')
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')

    if not end_date:
        end_date = None

    res_data = {"success": True}

    try:
        data = get_data(company, start_date=start_date, end_date=end_date, index_as_date=True, interval=DAY_INTERVAL)

        data_df = DataFrame(data)
        data_json_df = data_df.to_dict('index')

        data_array = []
        for key, value in data_json_df.items():
            data_array.append({
                'company_ticker': value['ticker'],
                'date': key,
                'open': value['open'],
                'high': value['high'],
                'low': value['low'],
                'close': value['close'],
                'adjclose': value['adjclose'],
                'volume': value['volume'],
            })

        res_data["data"] = YahooDataResponseSerializer(data_array, many=True).data
    except AssertionError:
        res_data["data"] = []

    return Response(data=res_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sp500_data(request):
    res_data = {"success": True}
    return Response(data=res_data, status=status.HTTP_200_OK)


class NasdaqView(viewsets.ModelViewSet):
    queryset = Nasdaq.objects.all()
    serializer_class = NasdaqSerializer

    # manual schema
    import_csv_response = openapi.Response('imported response', examples={
        "application/json": {
            "success": True,
        },
    })
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        '''
        insert a nasdaq row
        '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        '''
        get all cashflow list
        '''
        res_data = {
            "success": True,
            "data": NasdaqSerializer(self.get_queryset(), many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ImportCsvSerializer, parameters=None,
                         responses={status.HTTP_201_CREATED: import_csv_response})
    def import_csv(self, request, *args, **kwargs):
        importCsvSerializer = ImportCsvSerializer(data=request.data)
        if not importCsvSerializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # year = request.data.get('year')
        csv_file = request.data.get('csv')

        content = pd.read_csv(csv_file, header=None)
        content_dict = content.to_dict('index')
        for key, value in content_dict.items():
            serializer = self.serializer_class(data={
                "symbol": value[0],
                "company_name": value[1],
                "company_security_name": value[2],
            })
            serializer.is_valid(raise_exception=True)
            # serializer.save()

        return Response(status=status.HTTP_201_CREATED)
