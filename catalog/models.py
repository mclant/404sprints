from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField(null=True)

class Product(models.Model):
    PRODUCT_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=PRODUCT_CHOICES, default='I')
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(null=True) ##current in stock
    reorder_trigger = models.IntegerField(null=True)
    reorder_quantity = models.IntegerField(null=True)

    def image_url(self):
        return self.image_urls()[0]

    def image_urls(self):
        prodimages = ProductImage.objects.filter(product=self)
        urls = []
        for pi in prodimages:
            urls.append(pi.image_url())
        if not urls:
            urls.append(settings.STATIC_URL + 'catalog/media/products/image_unavailable.jpg')
        return urls

class ProductImage(models.Model):
    filename = models.TextField(null=True)
    product = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='images')

    def image_url(self):
        return settings.STATIC_URL + 'catalog/media/products/' + self.filename
    
