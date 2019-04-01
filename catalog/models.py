from django.db import models
from django.conf import settings
from decimal import Decimal

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
    


from decimal import Decimal
TAX_RATE = Decimal("0.05")

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
        # complete this method!
        self.subtotal = 0

        for si in SaleItem.objects.filter(sale=self, status='A'):
            self.subtotal = self.subtotal + (si.price * si.quantity)

        self.tax = self.subtotal * Decimal(0.05)
        self.tax = round(self.tax, 2)

        self.total = self.tax + self.subtotal
        self.total = round(self.total, 2)


    def finalize(self, stripeToken):
        '''Finalizes the sale'''
        # complete this method!
        # Ensure this sale isn't already finalized (purchased should be None)
        # Check product quantities one more time
        # Call recalculate one more time
        # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)
            # be sure to pip install stripe and import stripe into this file
        # Set purchased=now and charge_id=the id from Stripe
        # Save


class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    class Meta:
        ordering = [ 'product__name' ]