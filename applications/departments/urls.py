from django.contrib import admin
from django.urls import path

from . import views

app_name = 'department_app'

urlpatterns = [
    path(
        '', 
        views.Index.as_view(), 
        name="index"
    ),
    path(
        'departments-list/', 
        views.ListAllDepartments.as_view(), 
        name="all_departments"
    ),
    path(
        'new-department/', 
        views.RegisterDepartment.as_view(), 
        name='new_department'
    ),
]
