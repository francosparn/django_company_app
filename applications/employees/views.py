from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Employee

from .forms import RegisterForm


# Página de inicio
class Index(TemplateView):
    template_name = 'index.html'


# Listar todos los empleados 
class ListAllEmployees(ListView):
    template_name = 'employees/list_all.html'
    ordering = 'last_name'
    paginate_by = 5
    model = Employee
    context_object_name = 'employees'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        
        list = Employee.objects.filter(
            last_name__icontains=kword
        )
        
        return list


# Listar todos los empleados por área
class ListEmployeeByArea(ListView):
    template_name = 'employees/list_by_area.html'
    context_object_name = 'employees'

    def get_queryset(self):
        area = self.kwargs['short_name']
        
        list = Employee.objects.filter(
            department__short_name=area
        )
        
        return list


# Listar todos los empleados por trabajo
class ListEmployeeByJob(ListView):
    template_name = 'employees/list_by_job.html'
    context_object_name = 'employees'

    def get_queryset(self):
        area = self.kwargs['job']
        
        list = Employee.objects.filter(
            job=area
        )

        return list
    

# Listar todos los empleados 
class ListEmployeesAdmin(ListView):
    template_name = 'employees/list_employees.html'
    ordering = 'last_name'
    paginate_by = 10
    model = Employee
    context_object_name = 'employees'


# Filtro de búsqueda de empleados
class ListEmployeeByKword(ListView):
    template_name = 'employees/list_by_kword.html'
    context_object_name = 'employees'
    
    def get_queryset(self):
        keyword = self.request.GET.get('kword', '')
        
        list = Employee.objects.filter(
            first_name=keyword
        )

        return list


# Mostrar detalles del empleado
class EmployeeDetail(DetailView):
    template_name = 'employees/employee_detail.html'
    model = Employee


# Mensaje de éxito
class SuccessView(TemplateView):
    template_name = 'employees/success.html'


# Agregar empleado
class CreateEmployee(CreateView):
    template_name = 'employees/add_employee.html'
    model = Employee
    form_class = RegisterForm
    success_url = reverse_lazy('employee_app:success')


# Actualizar información de empleado
class UpdateEmployee(UpdateView):
    template_name = 'employees/update_employee.html'
    form_class = RegisterForm
    model = Employee
    success_url = reverse_lazy('employee_app:employees_admin')


# Eliminar empleado
class DeleteEmployee(DeleteView):
    template_name = 'employees/delete_employee.html'
    model = Employee
    success_url = reverse_lazy('employee_app:employees_admin')