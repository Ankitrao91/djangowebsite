from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = (
    (1,"Category 1"),
    (2,"Category 2"),
    (3,"Category 3")
)




class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self): 
        return self.desc

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.IntegerField(choices=CATEGORY, default=1)
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    launching_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', default="")
    is_active = models.IntegerField(default = 1, blank = True, null = True, help_text ='1->Active, 0->Inactive',  choices =(  (1, 'Active'), (0, 'Inactive') )) 
    class Meta:
        ordering = ['-launching_date']
    def __str__(self):
        return self.product_name

