from django_mako_plus import view_function
from django import forms
from catalog import models as cmod
from account import models as amod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, context):
    print('>>>>>>>>>>>.am i coming here')
    cart = request.user.get_shopping_cart()
    cart.recalculate()
    cart.save()
    si = cmod.SaleItem.objects.filter(sale=cart, status='A')

    context = {
        'cart': cart,
        'si': si,
    }

    return request.dmp.render('cart.html', context)


@view_function
def remove(request, sale_item: cmod.SaleItem):
    sale_item.status = 'D'
    sale_item.save()
    cart = request.user.get_shopping_cart()
    cart.recalculate()
    cart.save()

    return HttpResponseRedirect("/catalog/cart")
