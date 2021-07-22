from django.db import models


class Kospi(models.Model):
    date = models.DateField("날짜", max_length=10, null=False, unique=True)
    close = models.FloatField("종가", null=True)
    open = models.FloatField("시가", null=True)
