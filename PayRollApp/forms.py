from django import forms

from PayRollApp.models import Empolyee

from django.forms import modelform_factory

from PayRollApp.models import PartTimeEmpolyee

# Creating a Form based Model
# It should only be used if you want to generate html dynamically at run time

class EmployeeForm(forms.ModelForm):

    # To link form with the model
    class Meta:
        model=Empolyee

        # to use all the fields of Employee model for the EmployeeForm
        fields="__all__"

        # Customzing the date fields for EmployeeUpdate view and adding a date picker

        widgets = {

                'DOB' : forms.widgets.DateInput(attrs={'type': 'date'}),
                'HireDate' : forms.widgets.DateInput(attrs={'type': 'date'}),

        }

PartTimeEmpolyeeform=modelform_factory(PartTimeEmpolyee,fields=['Firstname','Lastname','Tilename'])

class DynamicPartTimeEmpolyeeform(PartTimeEmpolyeeform):
    def __init__(self,*args,**kwargs):
        super(DynamicPartTimeEmpolyeeform,self).__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget_attrs.pop("required",None)