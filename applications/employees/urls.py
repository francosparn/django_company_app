from django.contrib import admin
from django.urls import path

from . import views

app_name = 'employee_app'

urlpatterns = [
    path(
        '', 
        views.Index.as_view(), 
        name="index"
    ),
    path(
        'employees-list/', 
        views.ListAllEmployees.as_view(), 
        name="all_employees"
    ),
    path(
        'list-employee-by-area/<short_name>/', 
        views.ListEmployeeByArea.as_view(),
        name="area_employees"
    ),
    path(
        'list-employees-admin/', 
        views.ListEmployeesAdmin.as_view(),
        name="employees_admin"
    ),
    path(
        'list-employee-by-job/<job>/', 
        views.ListEmployeeByJob.as_view()
    ),
    path(
        'employee-search/', 
        views.ListEmployeeByKword.as_view()
    ),
    path(
        'employee-detail/<pk>/', 
        views.EmployeeDetail.as_view(), 
        name="employee_detail"
    ),
    path(
        'add-employee/', 
        views.CreateEmployee.as_view(),
        name="add_employee"
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name="success"
    ),
    path(
        'update-employee/<pk>/', 
        views.UpdateEmployee.as_view(), 
        name="update_employee"
    ),
    path(
        'delete-employee/<pk>/', 
        views.DeleteEmployee.as_view(), 
        name="delete_employee"
    ),
]
