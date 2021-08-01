from rest_framework import serializers
from stockapp.models import Kospi

class KospiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kospi
        fields = '__all__'