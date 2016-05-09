from django.contrib import admin
from videosearch.models import Platform, PlatformConfig,GeneralConfig, PlatformKeys, Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')

    list_filter = ['create_at']

admin.site.register(Platform)
admin.site.register(PlatformConfig)
admin.site.register(PlatformKeys)
admin.site.register(GeneralConfig)
admin.site.register(Task, TaskAdmin)
