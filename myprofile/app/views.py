from django.shortcuts import render

# Create your views here.
from .mail import Mail
def index(request):
	if request.method=='POST':
		pass
		ss=Mail(request.POST['name'],request.POST['email'],request.POST['subject'],request.POST['message'])
		# print('----------------------,,,,')
		print('---------->  ',request.POST['name'])
		ss.send_mail1()
		return render(request,'index.html')
	return render(request,'index.html')


def index1(request):
	return render(request,'inner-page.html')


def index2(request):
	return render(request,'portfolio-details.html')

def index3(request):
	return render(request,'forms/contact.php')