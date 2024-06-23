from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render
from .models import Message
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"] 
        password2 = request.POST["password2"] 
        email = request.POST["email"] 
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password does not match")


    return render(request, 'register.html', {})
    
    
    
from django.contrib.auth import authenticate
from django.shortcuts import redirect
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"] 
    
        auth_user = authenticate(username=username, password=password)

        if auth_user is not None:
            auth.login(request, auth_user)
            return redirect("/")
        else:
            messages.info(request, "incorrect credentials")
            
    return render(request, 'login.html', {})
    
    
def logout(request):
    auth.logout(request)
    return render(request, 'logout.html', {})


def home(request):
    return render(request, 'home.html', {})
    


def message_list(request):
    messages = Message.objects.filter(user= request.user)
    return render(request, 'list.html', {'message': messages})
    
from .forms import Messageform
def addMessage(request, username):
    get_user = User.objects.get(username=username)
    if request.method == "POST":
        form = Messageform(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = get_user
            var.save()
            messages.info(request, f"secret message have been sent to {get_user.username}")
            return redirect('register')
        else:
            messages.info(request, 'something went wrong')
            return redirect('register')
    else:
        get_user = User.objects.get(username=username)
        form = Messageform()
    return render(request, 'add.html', {'form' : form, 'get_user':get_user})
        

        
            
            
            
        
    
