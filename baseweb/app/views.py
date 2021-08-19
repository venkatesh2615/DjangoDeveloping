from django.shortcuts import render,redirect
from app.models import Login_model
from app.forms import LoginForm

# Create your views here.

def index(request):
	return render(request,'index.html')

def login(request):
	err=''
	myform=LoginForm()
	if request.method=='POST':
		myform=LoginForm(request.POST)
		if myform.is_valid():
			ss=Login_model.objects.create(**myform.cleaned_data)
			ss.save()
			myform=LoginForm()
			return redirect('/')

		else:
			err=request.POST
			return redirect('/login')




	return render(request,'login.html',{'form':myform,'err':err})