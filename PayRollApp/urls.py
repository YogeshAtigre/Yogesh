from django.urls import path
from .import views

urlpatterns = [

    path('Employeelist',views.Employeelist,name='Employeelist'),

    path('EmployeeDetails/<int:id>',views.EmployeeDetails,name='EmployeeDetails'),

    path('EmployeeDelete/<int:id>',views.EmployeeDelete,name='EmployeeDelete'),

    path('EmployeeUpdate/<int:id>',views.EmployeeUpdate,name='EmployeeUpdate'),

    path('EmployeeInsert',views.EmployeeInsert,name='EmployeeInsert')

]