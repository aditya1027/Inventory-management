from django.contrib import admin
from.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

#@admin.register(Desktop,Laptop,Mobile)
#class Viewadmin(admin.ModelAdmin):
#    pass

@admin.register(Desktop,Laptop,Mobile)
class Viewadmin(ImportExportModelAdmin):
    pass