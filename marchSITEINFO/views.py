from django.shortcuts import render
from .models import ContactUsFormModel, SiteInfoModel
from .forms import ContactUsForm

def ss(s):
    print(s, end='\n')


def aboutUsPage(request):

    site_information = SiteInfoModel.objects.first()
    print('#'*30)
    print(request.META.get('HTTP_REFERER'))
    print('#'*30)
    context = {
        'info' : site_information
    }

    return render(request, 'about.html', context)


def contactUsPage(request):

    if request.user.is_authenticated :
        init_info = {'sender':request.user, 'email':request.user.email}
    else:
        init_info = {}

    contactUsForm = ContactUsForm((request.POST or None), initial=init_info)
    site_information = SiteInfoModel.objects.first()

    if (request.method == 'POST') and ('sender' in request.POST) :


        
        # 
        # 
        # something is wrong with is valid part no prenthesis
        # 
        # 
        if contactUsForm.is_valid:
            
            contactUsForm = ContactUsForm(request.POST)
            contactUsForm.save()
            contactUsForm = ContactUsForm()
        else:
            
            contactUsForm.add_error(error='shit', field='message')


    context = {
        'info' : site_information,
        'form' : contactUsForm,
    }

    return render(request, 'contact.html', context)