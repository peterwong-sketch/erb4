from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name'] {'register)'}
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already taken')
            return redirect('register')
            if User.objects.filter(email=email).exists():
            messages.error(request,'email already taken')
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name, last_name=last_name)
            user.save()
            messages.success(request,  'You are now registered and can  log in')
            return redirect ('login')
    else:
            
            
            messages.error{request,'password do not match'}}
            return  redirect ('register')
    else:
        return render(request, 'accounts/register.html')
    
def login (request):
    if request.method  == 'POST':


# Create your views here.
