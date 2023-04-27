from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
def sign_in(request):
    if request.method == "GET":
        form=LoginForm()
        context={'form':form}
        return render(request, 'user/login.html', context)
    elif request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,'You\'ve Logged in successfully' )
                return redirect('web:index')
    messages.error(request, 'Invalid username or password')
    return render(request, 'user/login.html',{'form':form})
        


        


def sign_up(request):
    if request.method == "GET":
        form=RegisterForm()
        context={'form':form}
        return render(request, 'user/reg.html',context)
    elif request.method =="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user=form.username.lower()
            user.save()
            messages.success(request,'Tou have signed up sucessfully')
            login(request, user)
            return redirect('web:index')
        else:
            form=RegisterForm()
            return render(request, 'user/reg.html',{f'form':form})



def sign_out(request):
    logout(request)
    messages.success(request, f'You\'ve logged out successfully')
    return redirect('user:login')