from django.shortcuts import redirect, render

from django.contrib import auth

from django.contrib.auth.models import User

# Create your views here.

  
  

def login(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

  

        user = auth.authenticate(username = username , password = password)

  

        if user is not None:

            auth.login(request , user)

            return redirect('index')

        else:

            return redirect('login')

    return render(request , 'user/login.html')

  

def register(request):

        if request.method == 'POST':

            username = request.POST['username']

            email = request.POST['email']

            password = request.POST['password']

            repassword = request.POST['repassword']

            if password == repassword:

                if User.objects.filter(username = username).exists():

                    return redirect('register')

                else:

                    if User.objects.filter(email = email).exists():

                        return redirect('register')

                    else:

                        user = User.objects.create_user(username =username , password = password , email = email)
                        
                        user.save()

                        return redirect('login')

        return render(request , 'user/register.html')