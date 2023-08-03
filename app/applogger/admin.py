from django.contrib import admin

from applogger.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'user',
         'object',
        'description',
        'action_type',
        'time',
        'url',
        'data',
        'query',
       
    ]
    list_filter = ('user',
        'action_type',
        'time',
        'url',
        'object',
        'description',
        )
    search_fields = [
        'user',
        'action_type',
        'time',
        'url',
        'data',
        'query'
    ]
    # list_select_related = ['data', ]


admin.site.register(LogEntry,LogEntryAdmin)
