from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate, 
    login as logIn,
    logout, 
    get_user_model,
)
from ACCOUNTS.forms import (
    LoginForm,
    RegisterForm,
    )



def login_page(request):
    referer = request.META.get('HTTP_REFERER')

    # restrict (alredy logged in) users from accsesing this page
    if request.user.is_authenticated:
        return redirect('/')

    #custom FORMS instance
    login_form = LoginForm(request.POST or None)  



    if login_form.is_valid():

        #user login credentials
        user_name = login_form.cleaned_data.get('username')
        passWord = login_form.cleaned_data.get('password')
        myUser = authenticate(request, username=user_name, password=passWord)
        

        #if user is in database
        if myUser is not None:
            #login user with logIn builtin method
            logIn(request, myUser)
            #redirect the admin
            if myUser.id == 1:
                return redirect('/admin')
            #other users redirect
            # if prevpath:
            #     return redirect(prevpath)
            
            
            return redirect(request.META.get('HTTP_REFERER'))
    
        else:
            login_form.add_error('username', 'کاربری با مشخصات وارد شده پیدا نشد')

        print(f'2ND## form cleaned data is ###>> :{login_form.cleaned_data}\n{passWord}\n{user_name}\n')
    
    content = {
        'form' : login_form 
    }

    return render(request, 'login.html', content)
















def register_page(request):

    if request.user.is_authenticated:
        return redirect('/')

    registerform = RegisterForm(request.POST or None)

    if registerform.is_valid():
        email = registerform.cleaned_data.get('email')
        password = registerform.cleaned_data.get('password')

        newUser = User.objects.create_user(username=email, password=password, email=email)
        logIn(request, newUser)
        return redirect('/')
        
    

    content = {
        'form' : registerform
    }
    
    return render(request, 'register.html', content)



 













def log_ou(request):
    
    logout(request)
    
    return redirect(request.META.get('HTTP_REFERER'))