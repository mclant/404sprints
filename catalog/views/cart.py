from django_mako_plus import view_function
from django import forms
from catalog import models as cmod
from account import models as amod

@view_function
def process_request(request):

    cart = request.user.get_shopping_cart()
    si = cmod.SaleItem.objects.filter(sale=cart)

    context = {
        'cart': cart,
        'si': si,
    }

    return request.dmp.render('cart.html', context)

#class myForm(forms.Form):
