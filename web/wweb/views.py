from django.shortcuts import render,redirect
from .models import *
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
    form=Result.objects.all()
    context={"form":form}
    return render(request, 'results.html',context)

def add_result(request):    
    
    if request.method=="POST":
        roll_num=request.POST.get("roll_num")
        fl=request.POST.get("fl")
        sl=request.POST.get("sl")
        hindi=request.POST.get("hindi")
        ss=request.POST.get("ss")
        maths=request.POST.get("maths")
        science=request.POST.get("science")

        form=Result(roll_num=roll_num,fl=fl,sl=sl,hindi=hindi,ss=ss,maths=maths,science=science)
        form.save()
        data=Result.objects.all()
        context={"form":data}
        return redirect("/result",context)
    return render(request, 'add_result.html')

def view(request):
    form=Students.objects.all()
    context={'form':form}
    return render(request,'view.html',context)

def invoice(request,pk):
    form=Result.objects.get(id=pk)
    context={"form":form}
    return render(request,"invoice.html",context)

def delete_result(request):
    return render(request,"delete_result.html")