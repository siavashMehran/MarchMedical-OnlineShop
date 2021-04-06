from marchCOMMENTS.models import Comment
from django import forms


class CommentModelForm (forms.ModelForm):


    class Meta:
        model   = Comment
        fields  = ['user', 'user_email', 'comment_text', 'product']

        widgets = {
            'user'         : forms.TextInput(attrs={'placeholder' : 'نام'                }),
            'user_email'   : forms.TextInput(attrs={'placeholder' : 'ایمیل  (اختیاری) ' }),
            'comment_text' : forms.Textarea(attrs={'placeholder' : 'نظـر خود را بنویسیـد'           }),
            'product'      : forms.HiddenInput()
         }

