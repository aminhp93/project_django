from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
	users = User.objects.all()
	print(users)
	return render(request, "the_wall/index.html", {"users": users})

def new_user(request):

	return render(request, "the_wall/new_user.html")

def register(request):
	print(request)
	result = User.objects.validate_registration(request)
	print(result)
	if result[0] == False:
		return redirect("/user/new")
	return redirect("/")
