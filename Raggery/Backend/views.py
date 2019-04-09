from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homeView(request):
    if request.method =='GET':
        return render(request,'Backend/home.html')
def category(request):
    if request.method =='GET':
        return render(request,'Backend/category.html')   
def subcategory(request):
    if request.method =='GET':
        return render(request,'Backend/subcategory.html')
def productType(request):
    if request.method =='GET':
        return render(request,'Backend/product_type.html')   
def brand(request):
    if request.method =='GET':
        return render(request,'Backend/brand.html')
def productMaterial(request):
     if request.method =='GET':
        return render(request,'Backend/product_material.html')
def productSpecification(request):
     if request.method =='GET':
        return render(request,'Backend/product_specification.html')
def productSize(request):
    if request.method =='GET':
        return render(request,'Backend/product_size.html')    
def productTemplate(request):
    if request.method =='GET':
        return render(request,'Backend/product_template.html')
def productAdd(request):
    if request.method == 'GET':
        return render(request,'Backend/product_add.html')      
def stockReport(request):
    if request.method == 'GET':
        return render(request,'Backend/stock_report.html')  
def generalSetting(request):
    if request.method == 'GET':
        return render(request,'Backend/general_setting.html')   
                            