from .views import EmployeeView , DepartmentView
from django.urls import path


urlpatterns = [
    path('employees/' , EmployeeView.as_view() , name='All Employees'),
    path('employees/<int:emp_id>' , EmployeeView.as_view() , name='Employee'),
    path('employees/dept=<int:dept>' , EmployeeView.as_view() , name='Employee By View'),
    
    path('departments/' , DepartmentView.as_view() , name='Department')
]
