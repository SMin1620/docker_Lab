from django.urls import path, include

from stockapp.views import *

app_name = "stockapp"

urlpatterns = [
    path('api/kospi/', KospiAPIView.as_view(), name="kospiview"),
    path('chart', ChartView.as_view(), name="chart"),

]