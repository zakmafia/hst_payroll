from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist!')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print('Incorrect Credentials')
            
    return render(request, 'accounts/login_register.html')

# Deletes the session ID
def logoutUser(request):
    logout(request)
    return redirect('login')