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
            form.product = product
            if form.is_valid():
                quant = form.data['quantity']

                cart = request.user.get_shopping_cart()
                
                newitem = cmod.SaleItem(sale=cart, product=product, status='A', quantity=quant, price=product.price)
                newitem.save()

                si = cmod.SaleItem.objects.filter(sale=cart, status='A')

                context = {
                    'cart': cart,
                    'si': si,
                }

                print('>>>>>>>>>>> made it here')
                return HttpResponseRedirect('/catalog/cart', context)
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
    
    def clean(self):
        if int(self.cleaned_data.get('quantity')) > int(self.product.quantity):
            raise forms.ValidationError('Quantity not available')
        return self.cleaned_data
    
    