from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login,authenticate
from .forms import RegistrationForm
# Create your views here.

def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            e=request.POST
            # print('---------->',e)
            return render(request,'register/register.html',{'form':form,'msg':e})
        return redirect('/success')
    return render(request,'register/register.html',{'form':form,'msg':''})
    