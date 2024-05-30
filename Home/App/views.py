from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def header_footer(request):
    return render(request,'header_footer.html')