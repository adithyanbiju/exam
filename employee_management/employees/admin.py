from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "employee_id", "department", "designation", "salary")
    search_fields = ("name", "employee_id", "department")
