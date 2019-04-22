from django.db import models
# CATEGORY_STATUS=(('','--Select Category--'),('Active','Active'),('Inactive','Inactive'))

# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=40,unique=True)
    category_des=models.TextField()
    category_status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.category_name

class SubcategoryModel(models.Model):
    subcategory_name=models.CharField(max_length=40)
    category=models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING, default=1)
    subcategory_des=models.TextField()
    subcategory_status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subcategory_name

class ProductTypeModel(models.Model):
    product_type=models.CharField(max_length=40)  
    category=models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,default=1)
    subcategory=models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING,default=1)
    des=models.TextField()
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.product_type

class ProductMetarial(models.Model):
    metarial_name=models.CharField(max_length=50)
    category=models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,default=1)
    subcategory=models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING,default=1)
    product_type=models.ForeignKey(ProductTypeModel,on_delete=models.DO_NOTHING,default=1)
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.metarial_name

class BrandModel(models.Model):
    brand_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=40)
    founded_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    type_of_company=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    description=models.TextField()
    icon=models.ImageField(upload_to = 'brand_image/', default = 'brand_image/Blank-avatar.png')
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.brand_name

class ProductSpecificationModel(models.Model):
    name=models.CharField(max_length=40)
    category=models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,default=1)
    subcategory=models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING,default=1)
    product_type=models.ForeignKey(ProductTypeModel,on_delete=models.DO_NOTHING,default=1)
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ProductSizeModel(models.Model):
    name=models.CharField(max_length=40)
    category=models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,default=1)
    subcategory=models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING,default=1)
    product_type=models.ForeignKey(ProductTypeModel,on_delete=models.DO_NOTHING,default=1)
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class TemplateParentModel(models.Model):
    product_name=models.CharField(max_length=60)
    product_code=models.CharField(max_length=60)
    category=models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,default=1)
    subcategory=models.ForeignKey(SubcategoryModel,on_delete=models.DO_NOTHING,default=1)
    product_type=models.ForeignKey(ProductTypeModel,on_delete=models.DO_NOTHING,default=1)
    brand=models.ForeignKey(BrandModel,on_delete=models.DO_NOTHING,default=1)
    purchase_price=models.CharField(max_length=50)
    sale_price=models.CharField(max_length=50)
    off_price=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name

class TemplateMetarialChildModel(models.Model):
    template=models.ForeignKey(TemplateParentModel,on_delete=models.DO_NOTHING,default=1)
    metarial=models.ForeignKey(ProductMetarial,on_delete=models.DO_NOTHING,default=1)  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 
    


class TemplateSizeChildModel(models.Model):
    template=models.ForeignKey(TemplateParentModel,on_delete=models.DO_NOTHING,default=1)
    size=models.ForeignKey(ProductSizeModel,on_delete=models.DO_NOTHING,default=1)  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
  

class TemplateSpecificationChild(models.Model):
    template=models.ForeignKey(TemplateParentModel,on_delete=models.DO_NOTHING,default=1)
    specification=models.ForeignKey(ProductSpecificationModel,on_delete=models.DO_NOTHING,default=1)  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# class ProductAddModel(models.Model):
#     product_code=models.CharField(max_length=50)
#     template_parent=models.ForeignKey(TemplateParentModel,on_delete=models.DO_NOTHING,default=1)
#     product_qty=models.IntegerField()
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.product_code



      

    




