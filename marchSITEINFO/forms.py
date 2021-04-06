from django import forms
from .models import ContactUsFormModel
from django.core import validators


class ContactUsForm (forms.ModelForm):
    class Meta:
        model   = ContactUsFormModel
        fields  = ['title', 'email', 'message', 'sender']

        widgets = {
            'title'     : forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'عنوان پیام'         }),
            'sender'    : forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'نام'                 }),
            'email'     : forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'ایمیل  (اختیاری) '  }),
            'message'   : forms.Textarea (attrs={'class':'form-control' , 'placeholder' : 'متن پیام'            })
        }

