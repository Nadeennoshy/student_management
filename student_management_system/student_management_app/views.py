from django.contrib.auth import logout,login
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from student_management_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.urls.base import reverse

# Create your views here.
def ShowLoginPage(request):
    return render(request,"student_management_app/login.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                return HttpResponse("staff login")
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email+ "usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")