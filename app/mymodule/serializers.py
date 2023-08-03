from rest_framework import serializers
from .models import *
from datetime import datetime, date
from django_celery_results.models import TaskResult


# --------- записи для транскрибации

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        exclude = ['active']

class RecordQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False,help_text="имя записи")
    status = serializers.CharField(required=False,help_text="статус")
    description = serializers.CharField(required=False,help_text="описание")
    start_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")
    end_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")


class PutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id','name',]

class RecordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['name', 'id','file','status','description','time']

# --------- фоновые задачи



