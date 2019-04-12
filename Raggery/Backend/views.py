from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
# Create your views here.
def backendLogin(request):
        if request.method == 'POST':
                username=request.POST.get('username')
                password=request.POST.get('pwd')
                user=authenticate(username=username, password=password)
              
                if user is not None:
                        login(request, user)
                        # messages.success(request,'Welcome')
                        return HttpResponseRedirect(reverse('dashboard'))
                else:
                        # messages.warning(request,'Invalid User')
                        return HttpResponseRedirect(reverse('login'))
        else:
                if request.user.is_authenticated:
                        # messages.success(request,'Welcome Back')
                        return HttpResponseRedirect(reverse('backend'))

                return render(request,'Backend/login.html') 
def backendLoginout(request):
        logout(request)  
        return HttpResponseRedirect(reverse('login'))           
@login_required  
def homeView(request):
        if request.method =='GET':
                return render(request,'Backend/home.html')
@login_required
def category(request):
        if request.method =='GET':
                return render(request,'Backend/category.html')  
@login_required
def subcategory(request):
        if request.method =='GET':
                return render(request,'Backend/subcategory.html')

@login_required
def productType(request):
        if request.method =='GET':
                return render(request,'Backend/product_type.html')

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


                            