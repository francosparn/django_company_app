from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_name',
        'anulate',
    )

admin.site.register(Department, DepartmentAdmin)