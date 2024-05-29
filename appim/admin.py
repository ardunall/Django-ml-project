
from django.contrib import admin
from .models import Department, Doctor ,Service 

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'specialization')
    search_fields = ('name', 'title', 'specialization')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'description')
    search_fields = ('title', 'description')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Service, ServiceAdmin)
