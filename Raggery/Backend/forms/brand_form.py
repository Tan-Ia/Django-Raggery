from django import forms
from Backend.models import CategoryModel

class BrandForm(froms.ModelForm):
    class meta:
        model=BrandModel
        status_choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        fileds='__all__'
        widgets={
            'brand_name':forms.TextInput(attrs={'class':'form-control','placeholder':' Brand Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'eg.: email@email.com'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':' Brand Name'}),
            'founded_date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'type_of_company':forms.TextInput(attrs={'class':'form-control','placeholder':'Type Of Company'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'4','cols':'5','placeholder':'Product Type Description'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices),
        }
