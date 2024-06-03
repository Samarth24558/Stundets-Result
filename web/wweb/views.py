from django.shortcuts import render,redirect
from .models import Students
# Create your views here.

def index(request):
    return render(request,'index.html')

def manage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mname=request.POST.get('mname')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        course=request.POST.get('course')
        contact=request.POST.get('contact')

        data=Students(name=name,mother_name=mname,father_name=fname,address=address,gender=gender,date=dob,course=course,contact=contact)
        data.save()
        form=Students.objects.all()
        context={'form':form}
        return redirect('/view',context)
        
    return render(request,'manage.html')

def result(request):
    return render(request, 'results.html')

def add_result(request):
    return render(request, 'add_result.html')

def view(request):
    form=Students.objects.all()
    context={'form':form}
    return render(request,'view.html',context)
