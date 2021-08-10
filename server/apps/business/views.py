# import csv
# import io

# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
# from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import (Balance_sheet, Business_Basic_Info, Business_Condition, Business_Finance, Business_Preference,
                     Cashflow, Income_Statement)
from .serializers import (BalanceSheetSerializer, BusinessBasicSerializer, BusinessConditionSerializer,
                          BusinessFinanceSerializer, BusinessPreferenceSerializer, CashflowSerializer,
                          IncomeStatementSerializer)

# Create your views here.

CASHFLOW = 'cashflow'
BALANCE_SHEET = 'balance_sheet'
INCOME_STATEMENT = "income_statement"


def setData(kind, array):
    fileds = None
    if kind == CASHFLOW:
        fileds = Cashflow._meta.fields
    elif kind == BALANCE_SHEET:
        fileds = Balance_sheet._meta.fields
    elif kind == INCOME_STATEMENT:
        fileds = Income_Statement._meta.fields

    retData = {str(field).split('.')[2]: None for field in fileds}

    idx = 0
    for field in fileds:
        key = str(field).split('.')[2]

        if key == 'id' or idx >= len(array):
            continue

        retData[key] = array[idx]
        idx += 1

    return retData


# Create your views here.

class BusinessBasicView(GenericAPIView):
    serializer_class = BusinessBasicSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Business_Basic_Info.objects.all()
        # print(data)
        res_data = {
            "success": True,
            "data": BusinessBasicSerializer(data, many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class BusinessConditionView(GenericAPIView):
    serializer_class = BusinessConditionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Business_Condition.objects.all()
        # print(data)
        res_data = {
            "success": True,
            "data": BusinessConditionSerializer(data, many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class BusinessPreferenceView(GenericAPIView):
    serializer_class = BusinessPreferenceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):

        data = Business_Preference.objects.all()
        # print(data)
        res_data = {
            "success": True,
            "data": BusinessPreferenceSerializer(data, many=True).data,

        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class BusinessFinanceView(GenericAPIView):
    serializer_class = BusinessFinanceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):

        data = Business_Finance.objects.all()
        # print(data)
        res_data = {
            "success": True,
            "data": BusinessFinanceSerializer(data, many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class IncomeStatementView(GenericAPIView):
    serializer_class = IncomeStatementSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        res_data = {
            "success": True,
            "data": serializer.data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = Income_Statement.objects.all()
        # print(data)
        res_data = {
            "success": True,
            "data": IncomeStatementSerializer(data, many=True).data,

        }
        return Response(data=res_data, status=status.HTTP_200_OK)


class CashflowView(viewsets.ModelViewSet):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer

    # # manual schema
    # import_csv_response = openapi.Response('imported response', examples={
    #     "application/json": {
    #         "success": True,
    #     }
    # })
    # parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        '''
        insert a cashflow row
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
            "data": CashflowSerializer(self.get_queryset(), many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    # @ swagger_auto_schema(request_body=ImportCsvSerializer, parameters=None,
    # responses={status.HTTP_201_CREATED: import_csv_response})
    # def import_csv(self, request, *args, **kwargs):
    #     importCsvSerializer = ImportCsvSerializer(data=request.data)
    #     if not importCsvSerializer.is_valid():
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    #     year = request.data.get('year')
    #     csv_file = request.data.get('csv')

    #     data_set = csv_file.read().decode('UTF-8')
    #     io_string = io.StringIO(data_set)
    #     # next(io_string)

    #     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #         serializer = self.serializer_class(data=setData(CASHFLOW, column))
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()

    #     return Response(status=status.HTTP_201_CREATED)


class BalanceSheetView(viewsets.ModelViewSet):
    queryset = Balance_sheet.objects.all()
    serializer_class = BalanceSheetSerializer

    # manual schema
    # import_csv_response = openapi.Response('imported response', examples={
    #     "application/json": {
    #         "success": True,
    #     }
    # })
    # parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        '''
        insert a balance_sheet row
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
        get all balance_sheet list
        '''
        res_data = {
            "success": True,
            "data": BalanceSheetSerializer(self.get_queryset(), many=True).data,
        }
        return Response(data=res_data, status=status.HTTP_200_OK)

    # @ swagger_auto_schema(request_body=ImportCsvSerializer, parameters=None,
    # responses={status.HTTP_201_CREATED: import_csv_response})
    # def import_csv(self, request, *args, **kwargs):
    #     importCsvSerializer = ImportCsvSerializer(data=request.data)
    #     if not importCsvSerializer.is_valid():
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    #     year = request.data.get('year')
    #     csv_file = request.data.get('csv')

    #     data_set = csv_file.read().decode('UTF-8')
    #     io_string = io.StringIO(data_set)
    #     # next(io_string)

    #     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #         serializer = self.serializer_class(
    #             data=setData(BALANCE_SHEET, column))
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()

    #     res_data = {
    #         "success": True,
    #     }
    #     return Response(data=res_data, status=status.HTTP_200_OK)
