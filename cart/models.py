from django.db import models

from accounts.models import CustomUser
from products.models import  Product

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

user=models.Foreignkey(CustomUser, on_delete=models.CASCADE,related_name='cart_item')
product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_products')

quantity=models.PositiveIntegerField(default=1)
