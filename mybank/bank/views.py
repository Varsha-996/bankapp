
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Application




def home(request):
    return render(request, 'home.html')

def loginn(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return render(request,'new.html')
    else:
      return redirect('register')

  else:
    return render(request, 'login.html')


def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
      user=User.objects.create_user(username=username,password=password)
      user.save()
      return redirect('login')
    else:
      return redirect('register')

  else:
    return render(request, 'register.html')

def new(request):
  return render(request,'new.html')


  
def index(request):
    if request.method=='POST':
      name=request.POST.get('name','')
      age = request.POST.get('age', '')
      gender = request.POST.get('gender', '')
      dob =request.POST.get('dob', '')
      email = request.POST.get('email', '')
      phone= request.POST.get('phone', '')
      address= request.POST.get('address', '')
      application=Application(name=name,age=age,gender=gender,dob=dob,email=email,phone=phone,address=address)
      application.save()
    return render (request,'index.html')

