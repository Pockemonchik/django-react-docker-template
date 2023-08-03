import logging
from rest_framework.views import APIView
from django.http import JsonResponse
import traceback
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


logger = logging.getLogger(__name__)


class BaseView(APIView):
    """Базовый класс для всех view, обработка исключений"""
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    def initial(self, request, *args, **kwargs):
        """Добавляем лог для конкретных действий"""
        print(str(request.data))
        print(str(request.query_params))
        message = {
            "user": str(request.user),
            "url": str(request.META['PATH_INFO']),
            "action_type": str(request.method),
            "query": str(dict(request.query_params)),
            "data": str(request.data),
        }
        logger.info(message)
        super().initial(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)
            traceback_str = ''.join(traceback.format_tb(e.__traceback__))
            logger.error(str(e)+'\n'+traceback_str)
            return self._response({'error': str(e)}, status=400)
        if isinstance(response, (dict, list)):
            # print("base view")
            return self._response(response)
        else:
            # print("base view")
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(data, status=status)
