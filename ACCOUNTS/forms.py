from django import forms
from django.core import validators
from django.contrib.auth.models import User

class LoginForm (forms.Form):

    username = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder':'نام کاربری'}),
        label  = '',
        
    )

    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder':'پسورد'}),
        label  = '',

    )

    #username exists gets validated here then it goes to views
    #and runs the validators(if user == None) but since if this passes
    #the user object is never none there , that code is useless
    def clean_username(self):
        username = self.cleaned_data.get('username')
        userExists = User.objects.filter(username=username).exists()
        if not userExists:
            raise forms.ValidationError('نام کاربری اشتباه است')
        return username
            
        


class RegisterForm(forms.Form):

    email = forms.EmailField(
        widget     =  forms.EmailInput(attrs = {'placeholder':' example@gmail.com'}),
    
        label      =  'ایمیل',
 
        
    )

    password = forms.CharField(
        widget     =  forms.PasswordInput(attrs={'placeholder':'حداقل 7 کاراکتر'}),
        label      =  'رمز عبور',
        validators =  [
            validators.MinLengthValidator(limit_value=6, message='برای امنیت بیشتر اطلاعات شخصی شما رمز باید حداقل 6 کاراکتر باشد'),
        ],

    )
    password2 = forms.CharField(
        widget  =  forms.PasswordInput(attrs={'placeholder':'پسورد را دوباره وارد کنید'}),
        label   =  'تایید رمز عبور',
        
    )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        emailExists = User.objects.filter(email=email).exists()
        if emailExists:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده')
        return email
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2 :
            raise forms.ValidationError('رمز های وارد شده یکسان نیستند')
        

        return password
