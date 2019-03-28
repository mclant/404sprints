from django_mako_plus import view_function
from catalog import models as cmod
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })

@view_function
def process_request(request, product:cmod.Product):
    productimages = cmod.ProductImage.objects.filter(product=product)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = MyForm()


    context = {
        'product': product,
        'allProductImages': productimages,
    }
    return request.dmp.render('product.html', context)


class MyForm(forms.Form):
    quantity = forms.CharField(label="Quantity")
