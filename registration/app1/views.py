from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')


def SignupPage(request):
    
    if request.method=='POST':
        
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        user_exist=User.objects.filter(username = uname).exists()
        email_check=User.objects.filter(email=email).exists()
        print(email_check)
        
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        
        elif user_exist==True:
            messages.error(request, "This username is already taken")
            return redirect('/')
        
        elif email_check==True:
            messages.error(request, "This email is already taken")
            return redirect('/')
        
        
        
        else:
            my_user=User.objects.create_user(username = uname,email=email,password=pass1)
        
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')
        
        
        

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')















# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # Create your views here.

# @login_required(login_url='login')

# def HomePage(request):
#     return render (request,'home.html')


# def SignupPage(request):
    
#     if request.method=='POST':
        
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
        
#         if pass1!=pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
        
#         elif User.objects.filter(username = uname).first():
#             messages.error(request, "This username is already taken")
#             return redirect('login')
        
        
#         else:
#             my_user=User.objects.create_user(uname,email,pass1)
        
#             my_user.save()
#             return redirect('login')
#     return render (request,'signup.html')
        
        
        

# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")
#     return render(request,'login.html')

# def LogoutPage(request):
#     logout(request)
#     return redirect('login')


