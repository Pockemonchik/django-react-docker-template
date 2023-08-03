
import base64
import logging
import traceback
import config.settings as settings
from django.core.files import File
from .models import *
import json
import os

logger = logging.getLogger(__name__)

"""Помещаем сюда всю бизнес логику из Views"""