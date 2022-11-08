from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, Product
from django.contrib import messages
from .forms import UserForm,UserModelForm


# Create your views here.

def say_firstapp_hello(request):
    return render(request, 'hello.html')


def say_home_firstapp_hello(request):
    allOfUser = User.objects.all()
    allOfProduct = Product.objects.all()

    return render(request, "homeOfFirstapp.html", {'allOfUser': allOfUser, 'allOfProduct': allOfProduct})
def detail(request,name_id,slug):
    user=User.objects.get(id=name_id)

    return render(request,'detail.html',context={'user':user})

def delete(request,name_id):
    User.objects.get(id=name_id).delete()
    messages.success(request,'user deleted successfully','success')
    return redirect('home')

def creatUserForm(request):
    if request.method=='POST':

        form=UserForm(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create(id1=cd['id'],name=cd['name'],dateOfBirth=cd['dateOfBirth'])
            messages.success(request,"usre created succesfully","success")
            return  redirect('home')
    else:
        form=UserForm()

    return  render(request,'userForms.html',{'form':form})

def updateUser(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method=='POST':
        form=UserModelForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,f"user update {user_id} successfully","success")
            return redirect('details',user_id,user.name)

    else:
        form=UserModelForm(instance=user)
    return render(request,'updateUser.html',{'form':form})

