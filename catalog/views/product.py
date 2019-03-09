import Categories from categories as cmod

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product': product,
    })