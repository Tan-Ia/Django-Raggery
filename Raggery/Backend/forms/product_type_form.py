from django import froms
from Backend.models import ProductTypeModel
from Backend.models import CategoryModel
from Backend.models import SubcategoryModel

class ProductTypeFrom(froms.ModelForm):
    class Meta:
        model=ProductTypeModel
        category_choices=CategoryModel.objects.filter(category_status="Active")
        subcategory_choices=SubcategoryModel.objects.filter(subcategory_status="Active")
        status_choices=(('','--select'),('Active','Active'),('Inactive','Inactive'))
        fields='__all__'
        widgets={
            'product_type':froms.TextInput(attrs={'class':'form-control','placeholder':'Product Type Name'}),
            'category':froms.Select(attrs={'class':'form-control'},choices=category_choices),
            'subcategory':froms.Select(attrs={'class':'form-control'},choices=subcategory_choices),
            'des':froms.Textarea(attrs={'class':'form-control','rows':'4','cols':'5'}),
            'status':froms.Select(attrs={'class':'form-control'},choices=status_choices)
        }
