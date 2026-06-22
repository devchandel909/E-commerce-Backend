from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    is_active= models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    




