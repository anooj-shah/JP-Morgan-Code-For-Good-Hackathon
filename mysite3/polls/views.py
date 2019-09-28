from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def signupForm(request):
    return render(request, 'sInfo.html')



def get(request):
    context = {}
    ety = Representative.objects.all()
    name0 = ety[0].fname
    name1 = ety[1].fname
    name2 = ety[2].fname
    last0 = ety[0].lname
    last1 = ety[1].lname
    last2 = ety[2].lname
    context['first'] = name0
    context['second'] = name1
    context['third'] = name2
    context['l_first'] = last0
    context['l_second'] = last1
    context['l_third'] = last2
    return render(request, "sInfo.html", context)




