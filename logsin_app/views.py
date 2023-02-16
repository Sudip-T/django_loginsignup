from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Create your views here.
def log_in(request):
    if request.method=='GET':
        return render(request, 'log_in.html')
    else:
        username = request.POST['user_email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('success')

        else:
            messages.info(request, 'Invalid Email or Password')
            return render(request, 'log_in.html')


def log_out(request):
    logout(request)
    return render(request, 'log_in.html')


def success(request):
    return render(request, 'success.html')

def sign_up(request):
    user = get_user_model()
    print(user)
    if request.method=='GET':
        return render(request, 'sign_up.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']

        user.objects.create_user(full_name=username, email=email, password=password, phone_number=phone)

        return redirect('log_in')


def changepassword(request):
    if request.method=='GET':
        return render(request, 'changepassword.html')
    else:
        return render(request, 'changepassword.html')

@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status' : 400,
            'message' : 'key phone_number is required'
        })