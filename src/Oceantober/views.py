from django.shortcuts import render

def about(request):		
	return render(request, "about.html", {})

def blog(request):
	return render(request, "blog.html", {})

def awards(request):
	return render(request, "awards.html", {})