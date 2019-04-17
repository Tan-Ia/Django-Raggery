from django import forms
from Backend.models import ProductTypeModel
from Backend.models import CategoryModel
from Backend.models import SubcategoryModel
from Backend.models import ProductMetarial


class ProductMetarialForm(forms.ModelForm):
    class Meta:
        model=ProductMetarial
        category_choices=CategoryModel.objects.filter(category_status='Active')
        subcategory_choices=SubcategoryModel.objects.filter(subcategory_status='Active')
        product_type_choices=ProductTypeModel.objects.filter(status='Active')
        status_choices=(('','--select--'),('Active','Active'),('Inactive','Inactive'))
        fields='__all__'
        widgets={
            'metrial_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Metarial Name'}),
            'category':forms.Select(attrs={'class':'form-control'},choices=category_choices),
            'subcategory':forms.Select(attrs={'class':'form-control'},choices=subcategory_choices),
            'product_type':forms.Select(attrs={'class':'form-control'},choices=product_type_choices),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices)
        }

