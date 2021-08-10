# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import connection
from .serializers import UpdateUserSettingsSerializer

class UserSettingView(GenericAPIView):
    serializer_class = UpdateUserSettingsSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            res_data = {
                "success": True,
                "data": serializer.data,
            }
        except Exception as e:
            print(e)
            res_data = {
                "success": False,
                "data": "DB Error : {}".format(str(e)),
            }
        
        return Response(data=res_data, status=status.HTTP_200_OK)