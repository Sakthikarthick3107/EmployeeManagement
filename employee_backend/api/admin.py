from django.contrib import admin
from .models import Employee,Department
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept',]
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name'  , 'salary' , 'native']
    list_filter = ['dept']
    


admin.site.register(Employee , EmployeeAdmin)
admin.site.register(Department , DepartmentAdmin)
