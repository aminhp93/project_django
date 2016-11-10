from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "the_wall/index.html")

def create_user(request):
	return render(request, "the_wall/new_user.html")
