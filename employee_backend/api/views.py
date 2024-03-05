from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department , Employee
from .serializers import EmployeeSerializer , DepartmentSerializer



class DepartmentView(APIView):
    def get(self,request):
        depts = Department.objects.all()
        serializer = DepartmentSerializer(depts , many=True)
        return Response(serializer.data)


class EmployeeView(APIView):
    def get(self,request , emp_id = None , dept=None):
        if emp_id is not None:
            try:
                employee = Employee.objects.get(emp_id = emp_id)
                employee_serializer = EmployeeSerializer(employee)
                return Response(employee_serializer.data)
            except Employee.DoesNotExist:
                return Response({'message' : 'Employee Not Found'} , status=status.HTTP_404_NOT_FOUND)
        
        elif dept is not None:
            try:
                emp_dep = Employee.objects.filter(dept = dept)
                serializer = EmployeeSerializer(emp_dep,many=True)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({'message' : 'No employees working !'})
        
        employees = Employee.objects.all().order_by('-salary')
        employee_serializer = EmployeeSerializer(employees , many=True)
        return Response(employee_serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        new_data = EmployeeSerializer(data = request.data)
        if new_data.is_valid():
            new_data.save()
            return Response({'message' : 'Created successfully',
                             'data':new_data.data
                             } , status=status.HTTP_201_CREATED) 
        return Response(new_data.errors)
    
    
    def put(self,request ,  emp_id):
        employee = Employee.objects.get(emp_id=emp_id)
        
        updated_employee = EmployeeSerializer(employee , data=request.data)
        if updated_employee.is_valid():
            updated_employee.save()
            return Response({'message':'Updated successfully '})
        return Response(updated_employee.errors)
    
    def delete(self,request , emp_id):
        employee = Employee.objects.get(emp_id=emp_id)
        
        try:
            employee.delete()
            return Response({'message':'Deleted successfully'})
        except Employee.DoesNotExist:
            return Response({'error' : 'Not found'})
    



