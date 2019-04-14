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