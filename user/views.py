from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Shops
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Your Account Has Been Created! You Can Now LogIn')
			return redirect('login')
	else:
		form=UserRegisterForm()

	return render(request,"user/register.html",{"form":form})

def shop(request):
# 	# product1=Product()
# 	# product1.name="IRON MAN MASK (GLOW IN THE DARK) - MARVEL OFFICIAL T-SHIRT"
# 	# product1.desc="The artwork will be screen printed to perfection on our premium,regular fit 100% Cotton Redwolf branded tees that you know and love.."
# 	# product1.offer=True
	shops=Shops.objects.all()
	return render(request,"web/shop.html",{'shops':shops})
	# return render(request,"web/shop.html")
def profile(request):
	return render(request,"user/profile.html")
@login_required
def buy(request):
	messages.success(request,f'Order Placed Successfully!!!!')
	# messages.success(request,f"Don't Want To Buy More Then Please Logout Successfully" )
	return render(request,'web/order_placed.html')