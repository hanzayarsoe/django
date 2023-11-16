from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from . forms import SignUpForm,AddRecordForm
from . models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in successfully")
            return redirect('home')
        else:
            messages.success(request,"There was an error, Please try again")
            return redirect('home')
    else:
        return render(request,'index.html',{'records':records})
        

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'You have successfully Registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        records = Record.objects.get(id=pk)
        return render(request,'record.html',{'rec':records})
    else:
        messages.success(request,"You need to login first")
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request,"Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"You need to login first")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Record added successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You need to login first")
        return redirect('home')
    
def edit_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully")
            return redirect('home')
        return render(request,'edit_record.html',{'form':form})
    else:
        messages.success(request,"You need to login first")
        return redirect('home')