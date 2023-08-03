from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from config.settings import *
from .models import *
from config.settings import *
from core.views import BaseView
from rest_framework.parsers import MultiPartParser
from .services import *
from .tasks import *
from django_celery_results.models import TaskResult


class RecordListView(BaseView, LimitOffsetPagination):
    """Список записей или создание записи"""

    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(responses={200: RecordSerializer}, query_serializer=RecordQuerySerializer)
    def get(self, request):
        """Возвращает несколько записей"""
        serializer = RecordQuerySerializer(request.query_params)
        lang = serializer["lang"].value
        # если запрос по периоду
        if serializer["start_date"].value and serializer["end_date"].value:
            start_date = datetime.strptime(
                serializer["start_date"].value, "%d.%m.%Y")
            end_date = datetime.strptime(
                serializer["end_date"].value, "%d.%m.%Y")
            queryset = Record.objects.filter(
                time__lte=end_date, time__gte=start_date, name__contains=lang or "")
        else:
            queryset = Record.objects.filter(
             name__contains=lang or "")
       
        paginate_queryset = self.paginate_queryset(queryset, request, view=self)
        serializer = RecordListSerializer(
            instance=paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(responses={200: RecordSerializer}, request_body=RecordSerializer)
    def post(self, request):
        """Создание записи"""
        serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            lang = serializer.data['lang']
            id = int(serializer.data['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordDetailView(BaseView):
    """Получение, удаление, обновление конкретной записи"""

    @swagger_auto_schema(responses={200: RecordSerializer})
    def get(self, request, pk):
        """Возвращает конкретную запись"""

        queryset = Record.objects.get(id=pk)
        print(queryset.file.path)
        serializer = RecordSerializer(
            instance=queryset)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: PutSerializer}, request_body=PutSerializer)
    def put(self, request, pk):
        """Полное изменение записи"""
        record = Record.objects.get(id=pk)
        print(request)
        record.status = 'ready'
        serializer = PutSerializer(
            record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        """Изменение парметров записи"""

        return Response()

    @swagger_auto_schema(responses={200: RecordSerializer})
    def delete(self, request, pk):
        """Удалениие записи из базы"""
        try:
            record = Record.objects.get(id=pk)
            record.active = False
            record.save()
            return Response("delete "+str(pk), status=status.HTTP_200_OK)
        except:
            return Response(" cant delete "+str(pk), status=status.HTTP_400_BAD_REQUEST)
