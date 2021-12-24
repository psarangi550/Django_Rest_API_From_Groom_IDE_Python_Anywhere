from django.contrib import admin
from .models import WFMTTaskModel
# Register your models here.
@admin.register(WFMTTaskModel)
class WFMTTaskModelAdmin(admin.ModelAdmin):
    list_display=["id","cp_number","sne_id","scheme_number","trs","estimate"]
