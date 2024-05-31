from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def manage(request):
    return render(request,'manage.html')

def result(request):
    return render(request, 'results.html')
def add_result(request):
    return render(request, 'add_result.html')
