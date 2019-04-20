from django import forms
from Backend.models import ProductSizeModel
from Backend.models import CategoryModel


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model=ProductSizeModel
        fields='__all__'
        category_choices=CategoryModel.objects.filter(category_status='Active')
        status_choices=(('','--select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Size Name','id':'metarial_name'}),
            'category':forms.Select(attrs={'class':'form-control','id':'category'}),
            'subcategory':forms.Select(attrs={'class':'form-control','id':'subcategory'}),
            'product_type':forms.Select(attrs={'class':'form-control','id':'product_type'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=status_choices)

        }