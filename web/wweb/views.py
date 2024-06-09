from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        messages.error(request,"Invalid username or password")
    return render(request,"login.html")

def logOut(request):
    logout(request)
    return redirect("/login")


def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        rpassword=request.POST.get("rpassword")

        if password!=rpassword:
            messages.error(request,"Password not matched")
        else:
            User.objects.create_user(username=name,email=username,password=password)
            return redirect("/login")
    return render(request,"signup.html")


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    form=Result.objects.all()
    context={"form":form}
    return render(request,'index.html',context)

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
        messages.success(request,"Record added successfully")
        return redirect('/view',context)
        
    return render(request,'manage.html')

def result(request):
    form=Result.objects.all()
    context={"form":form}
    return render(request, 'results.html',context)

def add_result(request):    
    data=Students.objects.all()
    dict={"data":data}
    if request.method=="POST":        
        roll_num=request.POST.get("roll_num")
        if Result.objects.filter(roll_num=roll_num).exists():
            # print("Error")
            messages.error(request,"This Student data already exists in result. Try Again")
        
        else:
            fl=request.POST.get("fl")
            sl=request.POST.get("sl")
            hindi=request.POST.get("hindi")
            ss=request.POST.get("ss")
            maths=request.POST.get("maths")
            science=request.POST.get("science")
            stud_name=Students.objects.get(id=roll_num)
            form=Result.objects.create(roll_num=stud_name,fl=fl,sl=sl,hindi=hindi,ss=ss,maths=maths,science=science)
            form.save()
            data=Result.objects.all()
            context={"form":data}
            messages.success(request,"Record added successfully")            
            return redirect("/result",context)
    return render(request, 'add_result.html',dict)

def view(request):
    form=Students.objects.all()
    context={'form':form}
    return render(request,'view.html',context)

def delete_stud(request,pk):
    form=Students.objects.get(id=pk)
    context={"form":form}
    return render(request,"delete_stud.html",context)

def delete(request,pk):
    form=Students.objects.get(id=pk)
    form.delete()
    messages.success(request,"Record deleted successfully")
    return redirect("/view")

def invoice(request,pk):
    form=Result.objects.get(roll_num=pk)
    stud=Students.objects.get(id=pk)
    context={"form":form,'stud':stud}
    return render(request,"invoice.html",context)

def view_result(request):
    return render(request,"view_result.html")

def delete_result(request,num):
    form=Result.objects.get(roll_num=num)
    context={"data":form}
    return render(request,"delete_result.html",context)

def delete_res(request,num):
    form=Result.objects.get(roll_num=num)
    form.delete()
    messages.success(request,f" Sudent ID {num}'s Record deleted successfully")
    return redirect("/result")


def search_res(request):
    if request.method=="POST":
        num=request.POST.get("num")
        print(num)
        if num=="." or num==" " or num=="":
            messages.error(request,"Please enter valid student id")
        else:
            if not Result.objects.filter(roll_num=num).exists():
                messages.error(request,"Record not found")                
            else:
                form=Result.objects.get(roll_num=num)
                context={"form":form}
                return render(request,"view_result.html",context)

    return render(request,"view_result.html")

def update_stud(request,pk):
    data=Students.objects.get(id=pk)
    context={"data":data}    
    return render(request,"update_stud.html",context)

def update(request,pk):
    name=request.POST.get('name')
    mname=request.POST.get('mname')
    fname=request.POST.get('fname')
    address=request.POST.get('address')
    gender=request.POST.get('gender')
    dob=request.POST.get('dob')
    course=request.POST.get('course')
    contact=request.POST.get('contact')

    form=Students.objects.get(id=pk)
    form.name=name
    form.mother_name=mname
    form.father_name=fname
    form.address=address
    form.gender=gender
    form.date=dob
    form.course=course
    form.contact=contact
    form.save()
    messages.success(request,"Record updated successfully")
    return redirect("/view")


def update_result(request,num):
    data=Result.objects.get(roll_num=num)
    context={"data":data}
    return render(request,"update_res.html",context)

def updateres(request,num):
    fl=request.POST.get("fl")
    sl=request.POST.get("sl")
    hindi=request.POST.get("hindi")
    ss=request.POST.get("ss")
    maths=request.POST.get("maths")
    science=request.POST.get("science")
    form=Result.objects.get(roll_num=num)
    form.fl=fl
    form.sl=sl
    form.hindi=hindi
    form.ss=ss
    form.maths=maths
    form.science=science
    form.save()
    messages.success(request,"Record updated successfully")
    return redirect("/result")

