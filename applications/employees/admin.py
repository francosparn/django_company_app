from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'full_name',
        'passport',
        'email',
        'phone',
        'gender',
        'date_of_birth',
        'job',
        'department'
    )
    
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    list_filter = (
        'department',
        'job',
    )

    # Search filter by last name
    search_fields = (
        'last_name',
    )

admin.site.register(Employee, EmployeeAdmin)