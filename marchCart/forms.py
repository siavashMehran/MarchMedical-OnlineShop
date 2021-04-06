from django import forms



class OrderForm(forms.Form):


    product_id    = forms.CharField(widget=forms.HiddenInput())
    product_price = forms.IntegerField(widget=forms.HiddenInput())
    order_count   = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'search_box',}), initial=1)


    