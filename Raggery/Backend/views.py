from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms.category_form import CategoryForm
from .forms.subcategory_form import SubcategoryForm
from .forms.product_type_form import ProductTypeFrom
from .models import *
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
                product_add=ProductTypeFrom(request.POST)
                product_add.save()
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
                edit_data.save()
                messages.success(request,'Update Operation Successfull')
        else:
                edit_data=ProductTypeFrom(instance=product_data)
        context={
                'form':edit_data,
                
        }                
        return render(request,'Backend/product_type/product_type_update.html',context)        
# end product type method

@login_required
def brand(request):
        if request.method =='GET':
            return render(request,'Backend/brand.html')
@login_required
def productMaterial(request):
        if request.method =='GET':
                return render(request,'Backend/product_material.html')

@login_required
def productSpecification(request):
        if request.method =='GET':
                return render(request,'Backend/product_specification.html')

@login_required
def productSize(request):
        if request.method =='GET':
                return render(request,'Backend/product_size.html')  

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


                            