from django.shortcuts import render,redirect
from django.http import HttpResponse
from web.models import Contact
from datetime import datetime
from django.contrib import messages
from .models import Product
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
	# product1=Product()
	# product1.name="IRON MAN MASK (GLOW IN THE DARK) - MARVEL OFFICIAL T-SHIRT"
	# product1.desc="The artwork will be screen printed to perfection on our premium,regular fit 100% Cotton Redwolf branded tees that you know and love.."
	# product1.offer=True
	products=Product.objects.all()
	return render(request,"web/index.html",{'products':products})
def follow(request):
	return render(request,"web/followus.html")
def contact(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		desc=request.POST.get('desc')
		contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
		contact.save()
		messages.success(request, 'Your message has been sent!')

	return render(request,'web/contact.html')