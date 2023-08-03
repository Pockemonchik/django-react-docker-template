from logging import Handler

import json
import datetime
import random


class DBHandler(Handler):
    """Логирование определенных записей в бд"""
    model_name = None
    expiry = None

    def __init__(self, model="", expiry=0):
        super(DBHandler, self).__init__()
        self.model_name = model
        self.expiry = int(expiry)

    def emit(self, record):
        try:
            # instantiate the model
            try:
                model = self.get_model(self.model_name)
            except:
                from .models import LogEntry as model

            # import ast
            # message = ast.literal_eval(self.format(record))
            # log_entry = model(level="info",
            #                 user=message['user'],
            #                 url=message['url'],
            #                 action_type=message['action_type'],
            #                 query=message['query'],
            #                 data=message['data'],)
            # log_entry.save()

        except Exception as e:
            print(e)
            pass
    
   
    def get_model(self, name):
        names = name.split('.')
        mod = __import__('.'.join(names[:-1]), fromlist=names[-1:])
        return getattr(mod, names[-1])
