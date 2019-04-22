from django import forms
from Backend.models import TemplateParentModel
from Backend.models import CategoryModel
from Backend.models import TemplateMetarialChildModel
from Backend.models import TemplateSizeChildModel
from Backend.models import TemplateSpecificationChild
from Backend.models import BrandModel

class TemplateParentForm(forms.ModelForm):
    class Meta:
        model=TemplateParentModel
        fields='__all__'
        category_choices=CategoryModel.objects.filter(category_status='Active')
        brand_choices=BrandModel.objects.filter(status='Active')
        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Name','id':'product_name'}),
            'product_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Product Code','id':'product_code'}),
            'category':forms.Select(attrs={'class':'form-control','id':'category'}),
            'subcategory':forms.Select(attrs={'class':'form-control','id':'subcategory'}),
            'product_type':forms.Select(attrs={'class':'form-control','id':'product_type'}),
            'brand':forms.Select(attrs={'class':'form-control','id':'brand'}),
            'purchase_price':forms.TextInput(attrs={'class':'form-control','id':'purchase_price'}),
            'sale_price':forms.TextInput(attrs={'class':'form-control','id':'sale_price_id'}),
            'off_price':forms.TextInput(attrs={'class':'form-control','id':'off_price_id'}),  

        }
       
class TemplateMetarialChildForm(forms.ModelForm):
    class Meta:
        model=TemplateMetarialChildModel
        fields='__all__'
        widgets={
            'metarial':forms.Select(attrs={'class':'form-control valid','size':'5','multiple':'multiple','title':'Please select at least one browser','id':'browsers'})
        }
class  TemplateSizeChildForm(forms.ModelForm):
    class Meta:
        model=TemplateSizeChildModel
        fields='__all__'
        widgets={
            'size':forms.Select(attrs={'class':'form-control valid','size':'5','multiple':'multiple','title':'Please select at least one browser','id':'browsers'})
        } 
class  TemplateSpecificationFrom(forms.ModelForm):
    class Meta:            
        model=TemplateSpecificationChild
        fields='__all__'
        widgets={
            'specification':forms.Select(attrs={'class':'form-control valid','size':'5','multiple':'multiple','title':'Please select at least one browser','id':'browsers'})
        }
     