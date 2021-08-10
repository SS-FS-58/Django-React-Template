from rest_framework import serializers

from .models import Nasdaq

# Defines the available choices for Region, Language, and Range
REGION_CHOICES = []
LANG_CHOICES = []
RANGE_CHOICES = []


# Yahoo Stock & Market Request Serializers

# Sample API parameters: "q":"AMD", "region":"US"
class YahooAutoCompleteRequestSerializer(serializers.Serializer):
    q = serializers.CharField(required=True)
    region = serializers.CharField(required=True)


# Sample API parameters: "region":"US"
class YahooRegionRequest(serializers.Serializer):
    region = serializers.CharField(required=True)


# Sample API parameters: "symbol":"AMD"
class YahooSymbolRequest(serializers.Serializer):
    symbol = serializers.CharField(required=True)


# Yahoo Stock Request Serializers

# Sample API parameters: "symbols":"AMD", "region":"US"
class YahooStockRequestSerializer(serializers.Serializer):
    symbol = serializers.CharField(required=True)
    region = serializers.CharField(required=True)


# Yahoo Market Request Serializers

# Sample API parameters: "region":"US","symbols":"AMD,IBM,AAPL"
class YahooMarketQuotesRequest(serializers.Serializer):
    symbols = serializers.CharField(required=True)
    region = serializers.CharField(required=True)


# Sample API parameters: "region":"US","lang":"en-US","count":"6","start":"0"
class YahooMarketMoversRequest(serializers.Serializer):
    region = serializers.CharField(required=True)
    lang = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
    start = serializers.IntegerField(required=True)


# Sample API parameters: "symbols":"AMZN,AAPL,WDC,REYN,AZN,YM=F","interval":"1m","range":"1d"
class YahooMarketSparkRequest(serializers.Serializer):
    symbols = serializers.CharField(required=True)
    interval = serializers.CharField(required=True)
    _range = serializers.CharField(required=True)


# Sample API parameters: "q":"AMD", "region":"US"
class YahooMarketAutoCompleteRequest(serializers.Serializer):
    query = serializers.CharField(required=True)
    region = serializers.CharField(required=True)


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    replace = "range"
    replace_with = "_range"
    data_body = "data"
    try:
        kwargs[data_body][replace_with] = kwargs["data"].pop(replace)
    except KeyError:
        pass


# Sample API parameters: "region":"US","startDate":"1585155600000","endDate":"1589475600000","size":"10"
class YahooMarketEarningsRequest(serializers.Serializer):
    region = serializers.CharField(required=True)
    startDate = serializers.IntegerField(required=True)
    endDate = serializers.IntegerField(required=True)
    size = serializers.IntegerField(required=True)


# nzj code ---------------------------------------------------
class NasdaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nasdaq
        fields = '__all__'


class ImportCsvSerializer(serializers.Serializer):
    csv = serializers.FileField(max_length=None, allow_empty_file=False)


class YahooDataRequestSerializer(serializers.Serializer):
    company = serializers.CharField(required=True)
    start_date = serializers.CharField(required=True)
    end_date = serializers.CharField(required=False)


class YahooDataResponseSerializer(serializers.Serializer):
    company_ticker = serializers.CharField()
    date = serializers.DateTimeField()
    open = serializers.DecimalField(max_digits=None, decimal_places=6)
    high = serializers.DecimalField(max_digits=None, decimal_places=6)
    low = serializers.DecimalField(max_digits=None, decimal_places=6)
    close = serializers.DecimalField(max_digits=None, decimal_places=6)
    adjclose = serializers.DecimalField(max_digits=None, decimal_places=6)
    volume = serializers.DecimalField(max_digits=None, decimal_places=6)
