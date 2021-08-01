from rest_framework.routers import DefaultRouter

from django.urls import path, include
from stockapp import views as stockviews

from stockapp.views import KospiData, ChartView, KospiViewSet

app_name = "stockapp"

router = DefaultRouter()
router.register(r'post/', KospiViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('chart/', ChartView.as_view()),
    path('data/', KospiData),
]