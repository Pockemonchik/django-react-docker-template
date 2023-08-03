from django.contrib import admin
from django.contrib import admin

from mymodule.models import *

class RecordAdmin(admin.ModelAdmin):
    list_display = [
        'time',
        'name',
        'description',
        'file',
        'status'
       
    ]
    list_filter = (
        'time',
        'status',
        )
    search_fields = [
         'time',
        'name',
        'description',
        'file',
    ]



    


admin.site.register(Record,RecordAdmin)

# Register your models here.
