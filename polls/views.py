from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
l=[]
def index(request):
	if request.method=="POST":
		username=request.POST.get("usertxt")
		password=request.POST.get("userpass")
		user=authenticate(username=username,password=password)
		if user is not None:
		        login(request,user)
		        return redirect("in/")
		else:
		        return render(request,"login.html",{"message":"incorrect username or password"})    
	
	else:
	        data={}
	return render(request,"login.html",data)
def signup(request):
	if request.method=="POST":
		username=request.POST.get("usertxt")
		password1=request.POST.get("userpass1")
		password2=request.POST.get("userpass2")
		if password1==password2:
		     user=User.objects.create_user(username=username,password=password1)
		     return redirect("/")
		else:
		     return render(request,"signup.html",{"message":"Password does not match"})
        else:       
                data={}
                return render(request,"signup.html",data)
def ins(request):
       if request.method=="POST":
		item=request.POST.get("itemtxt")
		if item!="":
		     l.append(item)
		     data={"todo":l}
		     return render(request,"in.html",data)
       return render(request,"in.html",{"todo":l})
def out(request):      
       	logout(request.user)
        return render(request,"out.html",{})
def todo(request):      
        return render(request,"todo.html",{})
