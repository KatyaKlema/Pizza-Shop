from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from shopapp.forms import UserForm, UserFormForEdit # , ShopForm, 

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
	return redirect(shop_home)

@login_required(login_url='/shopapp/sign_in/')
def shop_account(request):
	user_form = UserFormForEdit(instance=request.user)
	#shop_form = ShopForm(instance=request.user.shit)

	if request.method == "POST":
		user_form = UserFormForEdit(request.POST, instance=request.user)
		#shop_form = ShopForm(request.POST, request.FILES, instance=request.user.shit)

		if user_form.is_valid(): #and shop_form.is_valid():
			user_form.save()
		#	shop_form.save()

	return render(request, 'shopapp/account.html', {
		'user_form': user_form,
		#'shop_form': shop_form
	})

@login_required(login_url='/shopapp/sign_in/')
def shop_shop(request):
    return render(request, 'shopapp/shop.html', {})

@login_required(login_url='/shopapp/sign_in/')
def shop_home(request):
    return redirect(shop_shop)

def shop_sign_up(request):
	user_form = UserForm()
	#shop_form = ShopForm()
	if request.method == "POST":
		user_form = UserForm(request.POST)
		#shop_form = ShopForm(request.POST, request.FILES)

		if user_form.is_valid(): # and shop_form.is_valid():
			new_user = User.objects.create_user(**user_form.cleaned_data)
			#new_shop = shop_form.save(commit=False)
			#new_shop.user = new_user
			#new_shop.save()

			login(request, authenticate(
				username = user_form.cleaned_data['username'],
				password = user_form.cleaned_data['password']
			))

			return redirect(shop_home)

	return render(request, 'shopapp/sign_up.html', {
        'user_form': user_form,
       # 'shop_form': shop_form
    })