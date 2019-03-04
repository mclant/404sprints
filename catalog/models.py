from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField

class Product(models.Model):
    PRODUCT_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=PRODUCT_CHOICES, default='I')
    name = models.TextField
    description = models.TextField
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField ##current in stock
    reorder_trigger = models.IntegerField
    reorder_quantity = models.IntegerField

    def image_url(self):
        url = settings.STATIC_URL + 'catalog/media/products/' + self.name

    def images_url(self):
        urls = []
        for pi in self.images.all():
            urls.append(pi.image_url())
        if not urls:
            return settings.STATIC_URL + 'catalog/media/products/image_unavailable.jpg'
        return urls

class ProductImage(models.Model):
    filename = models.TextField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='images')

    def image_url(self):
        return settings.STATIC_URL + 'catalog/media/products/' + self.filename
    
