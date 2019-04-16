from django import forms
from Backend.models import SubcategoryModel
from Backend.models import CategoryModel
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model=SubcategoryModel
        fields='__all__'
        category_choices=CategoryModel.objects.filter(category_status="Active")
        status_choices=(('','--select--'),('Active','Active'),('Inactive','Inactive'))
        # print("hksdhfkjsdhf")
        widgets={
            'subcategory_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Subcategory Name'}),
            'category':forms.Select(attrs={'class':'form-control'},choices=category_choices),
            'subcategory_des':forms.Textarea(attrs={'class':'form-control','placeholder':'Describe About Subcategory','rows':'4','cols':'5'}),
            'subcategory_status':forms.Select(attrs={'class':'form-control'},choices=status_choices)
        }