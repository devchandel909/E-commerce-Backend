from django.db import models

from django.conf import settings

#from accounts.models import CustomUser
from products.models import  Product




#user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='cart_item')
class Cart_item(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='cart_item')

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_products')

    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','product')
        

    def __str__(self):
        return ( f"{self.user.username}"
                f" - "
                f"{self.product.name}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''

RELATIONSHIPS
User → Cart Items
User
  ↓
Item1
Item2
Item3

One User → Many Cart Items

Product → Cart Items
iPhone
  ↓
User1 Cart
User2 Cart
User3 Cart

One Product → Many Cart Items

'''
    
