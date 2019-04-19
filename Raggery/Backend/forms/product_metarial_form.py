from django import forms
from Backend.models import ProductTypeModel
from Backend.models import CategoryModel
from Backend.models import SubcategoryModel
from Backend.models import ProductMetarial


class ProductMetarialForm(forms.ModelForm):
    class Meta:
        model=ProductMetarial
        category_choices=CategoryModel.objects.filter(category_status='Active')
   
        status_choices=(('','--select--'),('Active','Active'),('Inactive','Inactive'))
        fields='__all__'
        widgets={
            'metarial_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Metarial Name','id':'metarial_name'}),
            'category':forms.Select(attrs={'class':'form-control','id':'category'}),
            'subcategory':forms.Select(attrs={'class':'form-control','id':'subcategory'}),
            'product_type':forms.Select(attrs={'class':'form-control','id':'product_type'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices)
        }

