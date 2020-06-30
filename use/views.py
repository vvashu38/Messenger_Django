from django.shortcuts import render, redirect
from directmessages.apps import Inbox
from django.contrib.auth.models import User, auth
# Create your views here.
from django.contrib import messages
import json

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/loggedin")
        else:
            messages.info(request, "invalid credential")
            return redirect("/")
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'registration.html')


def loggedin(request):
    user = User.objects.get(username=request.user.username)
    user1 = User.objects.get(username='john')
    #user2 = User.objects.get(username='mridul')
    #Inbox.send_message(user, user1, "fhgfhf")
    a = Inbox.get_conversation(user, user1, 50 , True , True).values()
    list_result = [entry for entry in a]
    if request.is_ajax():
        increment = int(request.GET['append_increment'])
        increment_to = increment + 10
        return render(request, "logged.html", {'a': list_result[increment:increment_to] , 'user1': user1})
    else:
        return render(request, "logged.html", {'a' : list_result, 'user1' : user1})

def logout(request):
    auth.logout(request)
    return redirect('/')


