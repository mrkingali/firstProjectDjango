from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import  messages
from .forms import RegisterUserForm,LoginUserForm
from  django.contrib.auth import authenticate,login,logout


def registerUser(request):

    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['userName'],cd['emailAdress'],cd['password'])
            user.first_name=cd['firstName']
            user.last_name=cd['lastName']
            user.save()
            messages.success(request,"user successfully created",'success')
            return  redirect('home')

    else :
        form=RegisterUserForm()
    return render(request,'registerUser.html',{'form':form})

def loginUser(request):

    if request.method=="POST":
        form=LoginUserForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['userName'],password=cd['password'])

            if user is not None:
                login(request,user)
                messages.success(request,f' {user.first_name} loged in succesfully','success' )
                return redirect('home')
            else:
                messages.error(request,"user or password is wrong","danger")

    else :
        form=LoginUserForm()
    return render(request,'loginUser.html',{'form':form})

def logoutUser(request):

    messages.success(request,f"{request.user} logout successfully",'success')
    logout(request)
    return redirect('home')