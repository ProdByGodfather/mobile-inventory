from django.contrib import admin
from main.models import Mobile, Brand

class MobileAdminView(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'color', 'screen_size', 'status', 'manufacturing_country')
    list_filter = ('brand', 'status')
    search_fields = ('brand__name', 'model')
    

admin.site.register(Mobile, MobileAdminView)
admin.site.register(Brand)