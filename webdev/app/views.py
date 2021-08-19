from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item,ToDoList
from .forms import CreateList
# Create your views here.
def base(request):
    return render(request,'base.html',{'name':'BASE page test'})

def index(request,id):
    try:
        ls=ToDoList.objects.get(id=id)
        return render(request,'list.html',{'ls':ls})
    except:
    
        ls='This jira id is not present in list---- %s'%id
        return render(request,'index.html',{'ls':ls})


def home(request):
    return render(request,'index.html')

def create(request):
    myform=CreateList()
    if request.method=='POST':
        myform=CreateList(request.POST)
        if myform.is_valid():
            name=myform.cleaned_data['name']
            t=ToDoList(name=name)
            t.save()
            return HttpResponseRedirect('/%i'%t.id)
        pass
    return render(request,'create.html',{'form':myform})

def v1(request):
    return HttpResponse('<h1>Welcome to v1</h1>')

def success(request):
    return render(request,'success.html')