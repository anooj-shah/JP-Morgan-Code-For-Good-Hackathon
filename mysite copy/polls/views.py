from django.shortcuts import render
from .models import Info

def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def signupForm(request):
    return render(request, 'user_sign_up.html')

def addEntry(request):
    n = request.POST["InputFirstName"]
    inf = Info.objects.create(name=n)
    return render(request, 'index.html')




