from django import forms
from Backend.models import ProductTypeModel
from Backend.models import CategoryModel
from Backend.models import SubcategoryModel

class ProductTypeFrom(forms.ModelForm):
    class Meta:
        model=ProductTypeModel
        category_choices=CategoryModel.objects.filter(category_status="Active")
        subcategory_choices=SubcategoryModel.objects.filter(subcategory_status="Active")
        status_choices=(('','--select'),('Active','Active'),('Inactive','Inactive'))
        fields='__all__'
        widgets={
            'product_type':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Type Name'}),
            'category':forms.Select(attrs={'class':'form-control'},choices=category_choices),
            'subcategory':forms.Select(attrs={'class':'form-control'},choices=subcategory_choices),
            'des':forms.Textarea(attrs={'class':'form-control','rows':'4','cols':'5','placeholder':'Product Type Description'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices)
        }
