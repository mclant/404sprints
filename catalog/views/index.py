from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math
ITEMS_PER_PAGE = 3

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    products = cmod.Product.objects.filter(status="A")
    productimages = cmod.ProductImage.objects.all()

    if category is not None:
        products = products.filter(category=category)

    products = products[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]

    return request.dmp.render('index.html', {
        'category': category,
        'products': products,
        'page': page,
        'numpages': math.ceil(len(products) / ITEMS_PER_PAGE),
        'allProductImages': productimages,
    })

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('index.tile.html', {
        'product': product,
    })