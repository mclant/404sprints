from django_mako_plus import view_function
from catalog import models as cmod

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })

@view_function
def process_request(request, product:cmod.Product):
    productimages = cmod.ProductImage.objects.filter(product=product)

    context = {
        'product': product,
        'allProductImages': productimages,
    }
    return request.dmp.render('product.html', context)