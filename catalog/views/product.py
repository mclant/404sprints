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
        if request.user.is_authenticated:
            form = MyForm(request.POST)
            if form.is_valid():
                print('>>>>>>>>>>>' and form)
                return HttpResponseRedirect('/catalog/cart', {'product':product, 'form':form})
        else:
            return HttpResponseRedirect('/account/login')
    else:
        form = MyForm()


    context = {
        'product': product,
        'allProductImages': productimages,
        'form': form,
    }
    return request.dmp.render('product.html', context)


class MyForm(forms.Form):
    quantity = forms.CharField(label="Quantity")
    #product = cmod.Product.objects.get(name=product.name)
    '''
    def clean(self):
        if self.cleaned_data.get('quantity') > product.quantity:
            raise forms.ValidationError('Quantity not available')
    '''
    