from django.shortcuts import redirect, render
from PayRollApp.forms import EmployeeForm , PartTimeEmpolyeeform
from PayRollApp.models import Empolyee

# Create your views here.
def Employeelist(request):
    # This commented fucntion will get the data from Employee class/table
    #Employees=Empolyee.objects.all()

    #This will get the data from Employee class/table and also get the data from its foregin key which will intern fetch data from 
    # from Department and Country class/table
    Employees=Empolyee.objects.select_related('EmpDeparment','EmpCountry').all()

    # To print the query automatically created by django ORM
    # Note : this will print the data on cmd window 
    print(Employees.query)
    
    templatefilename='PayRollApp/Employees.html'
    Dict={"Employee":Employees}
    return render(request,templatefilename,context=Dict)

#####################################################################################################################################


def EmployeeDetails(request,id):
    
    # This commented fucntion will get the data from Employee class/table
    #Employees=Empolyee.objects.get(id=id)

    #This will get the data from Employee class/table and also get the data from its foregin key which will intern fetch data from 
    Employees=Empolyee.objects.select_related('EmpDeparment','EmpCountry').all().filter(id=id)
    

    print('EmployeeDetails query')
    print(Employees.query)

    templatefilename='PayRollApp/EmployeeDetails.html'

    #Here with Employees[0] we are trying to match the Deaprtment id in Employee class/table with department id in the Department table 
    #Same for Country 
    # This done because of laszy loading of ORM where the query is just created and kept but not submitted to database as it will only
    # be done if pass a iterator in html code or if you want fetch just a singel recodr at a time we can use the below method
    Dict={"EmployeeDetails":Employees[0]}
    return render(request,templatefilename,Dict)



######################################################################################################################################


def EmployeeDelete(request,id):

    ## This commented fucntion will get the data from Employee class/table
    #Empolyees=Empolyee.objects.get(id=id)

    #This will get the data from Employee class/table and also get the data from its foregin key which will intern fetch data from 
    Employees=Empolyee.objects.select_related('EmpDeparment','EmpCountry').all().filter(id=id)

    templatefilename='PayRollApp/EmployeeDelete.html'

    #Here with Employees[0] we are trying to match the Deaprtment id in Employee class/table with department id in the Department table 
    #Same for Country 
    # This done because of laszy loading of ORM where the query is just created and kept but not submitted to database as it will only
    # be done if pass a iterator in html code or if you want fetch just a singel recodr at a time we can use the below method
    Dict={"EmployeeDelete":Employees[0]}

    if request.method == "POST":
        Employees.delete()
        return redirect('Employeelist')

    return render(request,templatefilename,Dict)



#####################################################################################################################################


 
def EmployeeUpdate(request,id):

    #This commented fucntion will get the data from Employee class/table
    #Empolyees=Empolyee.objects.get(id=id)

    #This will get the data from Employee class/table and also get the data from its foregin key which will intern fetch data from 
    Empolyees=Empolyee.objects.select_related('EmpDeparment','EmpCountry').all().filter(id=id)

    templatefilename='PayRollApp/EmployeeUpdate.html'
    # Here it is required for a 'GET' as we are fecthing data from the database as giving it to the form
    #form = EmployeeForm(instance=Empolyees)

    # done on order get data from class/tables as we know in the above only a blank query is preprade and not submitted to database
    # and we will pass a blank data to instnace
    #form = EmployeeForm(instance=Empolyees)
    for emp in Empolyees:
        form = EmployeeForm(instance=emp)
        Dict={"form":form}

    # After you click submit button this below code will update the database
    if request.method == "POST":
        # done on order get data from class/tables as we know in the above only a blank query is preprade and not submitted to database
        # and we will pass a blank data to instnace
        # form = EmployeeForm(request.POST,instance=Empolyees)
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('Employeelist')

    return render(request,templatefilename,context=Dict)

######################################################################################################################################


def EmployeeInsert(request):
    templatefilename='PayRollApp/EmployeeInsert.html'
    #Creating an empty form as we will be inserting data
    form = EmployeeForm()
    Dict = {"form":form}
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Employeelist')

    return render(request,templatefilename,context=Dict)


#####################################################################################################################################

def BulkInsertDemo(request):
    extar_forms = 10

#This creates a list of forms (one for each employee) using the PartTimeEmployeeForm. Each form is pre-filled with data from request.POST (if a POST request is made) or with data from the corresponding employee's instance.
#The prefix is added to uniquely identify each form, where the prefix is set to employee-<employee.id> to avoid conflicts.
# intsead of using list comperssion you can alo use the below mentioned simple code
# forms = []
# for employee in employees:
#     form = PartTimeEmployeeForm(request.POST or None, instance=employee, prefix=f'employee-{employee.id}')
#     forms.append(form)


    forms = [PartTimeEmpolyeeform(request.POST or None,prefix=f'employee={i}')for i in range (extar_forms)]