from django.shortcuts import render

# Create your views here.
def homePage(request):
    if request.method == 'GET':
        return render(request,'Fontent/home.html')
