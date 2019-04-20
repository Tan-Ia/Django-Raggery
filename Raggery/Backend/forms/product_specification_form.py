from django import forms
from Backend.models import ProductTypeModel
from Backend.models import CategoryModel
from Backend.models import SubcategoryModel
from Backend.models import ProductSpecificationModel

class ProductSpecificationFrom(forms.ModelForm):
    class Meta:
        model=ProductSpecificationModel
        category_choices=CategoryModel.objects.filter(category_status='Active')
   
        status_choices=(('','--select--'),('Active','Active'),('Inactive','Inactive'))
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Specification Name','id':'metarial_name'}),
            'category':forms.Select(attrs={'class':'form-control','id':'category'}),
            'subcategory':forms.Select(attrs={'class':'form-control','id':'subcategory'}),
            'product_type':forms.Select(attrs={'class':'form-control','id':'product_type'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices)
        }