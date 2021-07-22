from time import strptime, mktime

from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from stockapp.models import Kospi


class KospiAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
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

        return Response(data)


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'stockapp/chart.html')