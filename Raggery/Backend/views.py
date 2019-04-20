from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms.category_form import CategoryForm
from .forms.subcategory_form import SubcategoryForm
from .forms.product_type_form import ProductTypeFrom
from .forms.product_metarial_form import ProductMetarialForm
from .forms.product_specification_form import ProductSpecificationFrom
from .forms.product_size_form import ProductSizeForm
from .forms.brand_form import BrandForm
from .models import *
from django.core import serializers
from Raggery.utils import render_to_pdf
# Create your views here.
# start coustom login  logout method
def backendLogin(request):
        if request.method == 'POST':
                username=request.POST.get('username')
                password=request.POST.get('pwd')
                user=authenticate(username=username, password=password)
              
                if user is not None:
                        login(request, user)
                        messages.success(request,'Welcome')
                        return HttpResponseRedirect(reverse('dashboard'))
                else:
                        messages.error(request,'Sorry Invalid User')
                        return HttpResponseRedirect(reverse('login'))
        else:
                if request.user.is_authenticated:
                        messages.warning(request,'Welcome Back')
                        return HttpResponseRedirect(reverse('backend'))

                return render(request,'Backend/login.html') 
def backendLoginout(request):
        logout(request)  
        return HttpResponseRedirect(reverse('login'))    
#  end login logout method   

# start home view method           
@login_required  
def homeView(request):
        if request.method =='GET':
                return render(request,'Backend/home.html')
# end home view method

# start category add method                
@login_required
def category(request):
        category_all_data=CategoryModel.objects.all()
        if request.method =='POST':
                category_data=CategoryForm(request.POST)
                if category_data.is_valid():
                        category_data.save()
                        messages.success(request,'Form submission successful')
                        return HttpResponseRedirect(reverse('category'))
                
        else:
                category_data=CategoryForm()
        context={
                'form':category_data,
                'category_data':category_all_data
        }        
        return render(request,'Backend/category/category.html',context) 

# end category add method  

# start category delete method
@login_required
def category_delete(request,pk):
        category_delete_data=get_object_or_404(CategoryModel,pk=pk)
        category_delete_data.delete()
        messages.info(request,'Category Date Deleted')
        return HttpResponseRedirect(reverse('category')) 
# end category delete method

# start category update method
@login_required
def category_update(request,pk):
        category_update_data=get_object_or_404(CategoryModel,pk=pk)
        if request.method == 'POST':
                form=CategoryForm(request.POST or None,instance=category_update_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Category Data Save Successfully")
                        return redirect('category_update',pk=pk)
        else:
                form=CategoryForm(instance=category_update_data)
        context={
                'form':form,
                
        }        
        return render(request,'Backend/category/category_update.html',context)

# end category update method        

# start category status update method
@login_required
def category_status(request,pk):
        category_status_data=get_object_or_404(CategoryModel,pk=pk)
        if category_status_data.category_status == 'Active':
                category_status_data.category_status='Inactive'
                messages.info(request,'Successfully Category Changed Into Inactive')
        else:
               category_status_data.category_status='Active'
               messages.success(request,'Successfully Updated status Into Active')
        category_status_data.save()     
                       
        return HttpResponseRedirect(reverse('category'))  
# end category status update method

# start category pdf method
def category_pdf(request):
        category_data=CategoryModel.objects.all()
        pdf=render_to_pdf('Backend/category/category_pdf.html',{'category_data':category_data})
        return HttpResponse(pdf,content_type="application/pdf")
# end category pdf method

# start category download method
def category_download(request):
        # brand_data = Company.objects.order_by('-id')
        # pdf = render_to_pdf('backend/Brand/brand_pdf.html', {'brand_data': brand_data})
        # if pdf:
        #         response = HttpResponse(pdf, content_type='application/pdf')
        #         filename = f"Company_{date.today()}"
        #         content = "attachment; filename='%s'" % (filename)
        #         response['Content-Disposition'] = content
        # return response
        return HttpResponse("Not found")
# end category download method

# start subcategory method

@login_required
def subcategory(request):
        all_data=SubcategoryModel.objects.all()
        if request.method =='POST':
                subcategory_form=SubcategoryForm(request.POST)
                if subcategory_form.is_valid():
                        subcategory_form.save()
                        messages.success(request,'Subcategory Data Save Sucessfully')
                        return HttpResponseRedirect(reverse('subcategory'))
        else:
           
                subcategory_form=SubcategoryForm()

        context={
                'form':subcategory_form,
                'subcategory_data':all_data
        }   
        return render(request,'Backend/subcategory/subcategory.html',context)  

def subcategory_status(request,pk):
        subcategory=get_object_or_404(SubcategoryModel,pk=pk)
        if subcategory.subcategory_status =="Active":
                subcategory.subcategory_status="Inactive"
                messages.warning(request,"Status Inactive Successfully")
        else:
                subcategory.subcategory_status="Active"
                messages.success(request,"Status Active Successfully")
        subcategory.save()                
        return HttpResponseRedirect(reverse('subcategory'))

def subcategory_delete(request,pk):
        subcategory_data=get_object_or_404(SubcategoryModel,pk=pk)
        subcategory_data.delete()
        messages.warning(request,"Delete Data Successfully")
        return HttpResponseRedirect(reverse('subcategory'))
        
def subcategory_update(request,pk):
        subcategory_data=get_object_or_404(SubcategoryModel,pk=pk)
        if request.method == 'POST':
                subcategory_update=SubcategoryForm(request.POST or None,instance=subcategory_data)
                if subcategory_update.is_valid():
                        subcategory_update.save()
                        messages.success(request,'Update Operation Successful')
                        return redirect('subcategory_update',pk=pk)
        else:
                subcategory_data=SubcategoryForm(instance=subcategory_data)
        context={
                'form':subcategory_data
        }       
        return render(request,'Backend/subcategory/subcategory_update.html',context)               
# end subcategory method

# start product type method
@login_required
def productType(request):
        product_type_data=ProductTypeModel.objects.all()
        if request.method =='POST':
                product_type=ProductTypeFrom(request.POST)
                if product_type.is_valid():
                        product_type.save()
                        messages.success(request,'Product Type Save Successfully')
                        return HttpResponseRedirect(reverse('producttype'))
        else:
                product_type=ProductTypeFrom()
        context={
                'form':product_type,
                'all_data':product_type_data
        }                
        return render(request,'Backend/product_type/product_type.html',context)
def product_status(request,pk):
        product_data=get_object_or_404(ProductTypeModel,pk=pk)
        # product=ProductTypeModel.objects.filter(pk=pk)
        if product_data.status == "Active":
                product_data.status='Inactive'
                messages.warning(request,'Status Inactive Successfully')
        else:
                product_data.status='Active'
                messages.success(request,"Status Active Successfully")
        product_data.save()  
        # print(product.subcategory)              
        return HttpResponseRedirect(reverse('producttype'))      

def product_delete(request,pk):
        product_data=get_object_or_404(ProductTypeModel,pk=pk)
        product_data.delete()
        messages.warning(request,'Delete Operation Successfull')
        return HttpResponseRedirect(reverse('producttype'))

def product_update(request,pk):
        product_data=get_object_or_404(ProductTypeModel,pk=pk)
        if request.method == 'POST':
                edit_data=ProductTypeFrom(request.POST or None,instance=product_data)
                if edit_data.is_valid():
                        edit_data.save()
                        messages.success(request,'Update Operation Successfull')
                        return redirect('product_update',pk=pk)
        else:
                edit_data=ProductTypeFrom(instance=product_data)
        context={
                'form':edit_data,
                
        }                
        return render(request,'Backend/product_type/product_type_update.html',context)        
# end product type method
# start  brand method
@login_required
def brand(request):
        brand_data=BrandModel.objects.all()
        if request.method =='POST':
                form_data=BrandForm(request.POST,request.FILES)
                print(form_data)
                if form_data.is_valid():
                        form_data.save();
                        messages.success(request,'Save Operation Successfully Done')
                        return HttpResponseRedirect(reverse('brand'))
        else:
                form_data=BrandForm()
                # data='ok'
        context={
                'form':form_data,
                'brand_data':brand_data
        }        
                
        return render(request,'Backend/brand/brand.html',context)
# end  brand method
# start product metarial method



def getSubcategory(request):
        category=request.POST.get('category')
        subcategory=SubcategoryModel.objects.filter(category=category)
        value = serializers.serialize('json', subcategory)
        return HttpResponse(value, content_type="application/json")

def getProducttype(request):
        subcategory=request.POST.get('subcategory')   
        product_type=ProductTypeModel.objects.filter(subcategory=subcategory)  
        value_return=serializers.serialize('json',product_type) 
        return HttpResponse(value_return,content_type="application/json")  
        
@login_required   
def productMaterial(request):
        product_metarial=ProductMetarial.objects.all()
        if request.method =='POST':
                metarial_form=ProductMetarialForm(request.POST)
                if metarial_form.is_valid():
                        metarial_form.save()
                        messages.success(request,'Metarial Data Save Succsessfully')
                        return HttpResponseRedirect(reverse('material'))

        else:
                metarial_form=ProductMetarialForm()
        context={
                'form':metarial_form,
                'all_data':product_metarial
        }        
        return render(request,'Backend/product_metarial/product_material.html',context)

def productMetarialDelete(request,pk):
       delete_data=get_object_or_404(ProductMetarial,pk=pk)
       delete_data.delete()
       messages.warning(request,'Delete Operation Successfull')
       return HttpResponseRedirect(reverse('material'))    

def productMetarialUpdate(request,pk):
         get_update_data=get_object_or_404(ProductMetarial,pk=pk)
         if request.method =='POST':
                 update_data=ProductMetarialForm(request.POST or None,instance=get_update_data)
                 if update_data.is_valid():
                         update_data.save()
                         messages.success(request,'Update Operation Successfull')
                         return redirect('product_metarial_update',pk=pk)
                         
         else:
                update_data=ProductMetarialForm(instance=get_update_data)
         context={
                'form':update_data
                
          }
         return render(request,'Backend/product_metarial/product_metarial_update.html',context)       


# end product metarial method 
# start product specification method 
@login_required
def productSpecification(request):
        all_data=ProductSpecificationModel.objects.all()
        if request.method =='POST':
                form_data=ProductSpecificationFrom(request.POST)
                if form_data.is_valid():
                        form_data.save()
                        messages.success(request,'Save Operation Succsesful')
                        return HttpResponseRedirect(reverse('specification'))
        else:

                form_data=ProductSpecificationFrom()
        context={
                'form':form_data,
                'all_data':all_data
        }        
        return render(request,'Backend/product_specification/product_specification.html',context)
# end product specification method 
@login_required
def productSize(request):
        all_data=ProductSizeModel.objects.all()
        if request.method =='POST':
                form_data=ProductSizeForm(request.POST)
                if form_data.is_valid():
                        form_data.save()
                        messages.success(request,'Save Operation Succsessfully Done')
                        return HttpResponseRedirect(reverse('size'))
        else: 
                form_data=ProductSizeForm()  
        context={
                'form':form_data,
                'all_data':all_data
        }             
        return render(request,'Backend/product_size/product_size.html',context)  

@login_required
def productTemplate(request):
        if request.method =='GET':
                return render(request,'Backend/product_template.html')

@login_required
def productAdd(request):
        if request.method == 'GET':
                return render(request,'Backend/product_add.html')    

@login_required
def stockReport(request):
        if request.method == 'GET':
                return render(request,'Backend/stock_report.html') 

@login_required
def generalSetting(request):
        if request.method == 'GET':
                return render(request,'Backend/general_setting.html')


                            