from django.contrib import admin
from bbcure.models import CureData

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')

    list_filter = ['create_at']

admin.site.register(CureData)
