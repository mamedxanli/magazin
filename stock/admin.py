from django.contrib import admin
from stock.models import Clothes
from import_export.admin import ImportExportModelAdmin


@admin.register(Clothes)
class ViewAdmin(ImportExportModelAdmin):
    pass

#admin.site.register(Clothes)

