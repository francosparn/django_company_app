from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.employees.models import Employee

from .models import Department
from .forms import NewDepartmentForm

# Listar todos los departamentos de la empresa
class ListAllDepartments(ListView):
    template_name = 'departments/list_all.html'
    model = Department
    context_object_name = 'departments'


# Registrar un departamento
class RegisterDepartment(FormView):
    template_name = 'departments/new_department.html'
    form_class = NewDepartmentForm
    success_url = '/'

    def form_valid(self, form):
        dept = Department(
            name=form.cleaned_data['name'],
            short_name=form.cleaned_data['short_name']
        )
        dept.save()
    
        return super(RegisterDepartment, self).form_valid(form)