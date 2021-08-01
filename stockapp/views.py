from time import strptime, mktime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

from stockapp.models import Kospi
from stockapp.serializers import KospiSerializer


def KospiData(request):
    stocks = Kospi.objects.all().order_by('date')

    close_list = []
    open_list = []

    for stock in stocks:
        times = strptime(str(stock.date), '%Y-%m-%d')
        utc_now = mktime(times) * 1000

        close_list.append([utc_now, stock.close])
        open_list.append([utc_now, stock.open])

    data = {
        'close': close_list,
        'open': open_list,
    }

    return JsonResponse(data)

    
class KospiViewSet(ModelViewSet):
    queryset = Kospi.objects.all()
    serializer_class = KospiSerializer


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'stockapp/chart.html')