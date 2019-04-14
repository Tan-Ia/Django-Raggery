from django import forms
from Backend.models import CategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'category_name':forms.TextInput(attrs={'class':'form-control'}),
            'category_des':forms.Textarea(attrs={'class':'form-control','rows':'4','cols':'5'}),
            'category_status':forms.Select(attrs={'class':'form-control'},choices=choices)

        }

