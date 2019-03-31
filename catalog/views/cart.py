from django_mako_plus import view_function
from django import forms
from catalog import models as cmod
from account import models as amod

@view_function
def process_request(request, product:cmod.Product):
    
    cart = request.user.get_shopping_cart()
    '''
    for item in si:
        if item.name == product.name:
            quantity = product.quantity - item.quantity
    
    if not quantity:
        quantity = product.quantity
    '''

    newitem = cmod.SaleItem(sale=cart, product=product, status='A', quantity=product.quantity, price=product.price)
    newitem.save()

    si = cmod.SaleItem.objects.filter(sale=cart)

    context = {
        'cart': cart,
        'si': si,
    }

    return request.dmp.render('cart.html', context)

#class myForm(forms.Form):
