from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    birthdate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)

    def get_shopping_cart(self):
            from catalog import models as cmod
            shopping_cart = cmod.Sale.objects.get(user=self)
            print('>>>>>>>>>>still trying')
            # retrieve (or create) a Sale with purchased=None for this user
            if not shopping_cart:
                shopping_cart = cmod.Sale(user=self)
                shopping_cart.save()
                print('>>>>>>>this is where it should create the new shopping cart')


            # return the Sale object
            
            return shopping_cart
            