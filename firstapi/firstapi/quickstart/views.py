from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request,'index.html')

def extraPage(request):
    return render(request, 'extra.html')