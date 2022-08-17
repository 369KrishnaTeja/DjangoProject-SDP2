from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
import numpy as np
import random
from . import models
import secrets

secrets.token_hex(4)
ranvc = random.randint(999, 9999)


def home(request):
    page_title = "Home"
    return render(request, 'home.html', {'page_title': page_title})


def bidding(request):
    page_title = "Bidding"
    return render(request, 'bid.html', {'page_title': page_title})


def features(request):
    page_title = "Features"
    return render(request, 'features.html', {'page_title': page_title})


# Create your views here.
def register(request):
    if request.method == 'POST':
        n = request.POST['user']
        p = request.POST['pass']
        q = request.POST['full']
        s = request.POST['email']
        user = User.objects.create_user(username=n, password=p, first_name=q, email=s)
        user.save()
        print("user created")
        subject = 'Welcome to BAG world'
        message = f'Hi {user.username}, thank you for registering in our BAG.\n' \
                  f'Click on the Link below and Verify to Login to your account \n' \
                  f'Enter the below provided code \n' \
                  f'NOTE : Please enter the code correctly , if you make mistake while entering wait for the another code\n' \
                  f'{ranvc}\n ' \
                  f'http://127.0.0.1:8000/verifycode/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse(f"Registered successfully ,Please verify your email\n"
                            f"* <a href='https://mail.google.com'>Gmail</a>\n"
                            f"* <a href='https://in.search.yahoo.com'>yahoo</a>\n"
                            f"* <a href='https://outlook.office365.com/mail/'>Outlook</a>")
    else:
        return render(request, "reg.html")


def user_login(request):
    if request.method == 'POST':
        n = request.POST['user']
        p = request.POST['pass']
        user = auth.authenticate(username=n, password=p)
        if user is not None:
            auth.login(request, user)
            return render(request, "home.html")
        else:
            return render(request, "login.html", )
    else:
        return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("Home")
def about(request):
    return render(request,'about.html')


def verificationcode(request):
    t = "Please verify "
    if request.method == 'POST':
        c = request.POST['captcha']
        c = int(c)
        if c == ranvc:
            return HttpResponse(f"Verified successfully ,Please Login to your account\n"
                                f"* <a href='http://127.0.0.1:8000/login/'>Login</a>\n")
        else:
            return render(request, 'Codeverification.html')
    return render(request, 'Codeverification.html')


def display(request):
    st1 = models.User1.objects.all()
    # st1=models.User1.objects.values('username')
    return render(request, 'data.html', {'st1': st1})
# subject = 'Captcha Error Notification!!'
#        message = f'Dear User,We noticed that you have entered the wrong code.\n' \
#                 f'Click on the Link below again and Verify to Login to your account \n' \
#                f'Enter the below provided code perfectly\n' \
#               f'{ranvc}\n ' \
#              f'http://127.0.0.1:8000/verifycode/'
#   email_from = settings.EMAIL_HOST_USER
#  recipient_list = [user.email]
# send_mail(subject, message, email_from, recipient_list)
