from django.contrib import admin

# Register your models here.
from django.contrib import admin
from jobs.models import Location, Job

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'country')

admin.site.register(Location, LocationAdmin)

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobAdmin)
