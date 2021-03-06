from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#class extra_user_info(models.Model):
 #   usr = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
  #  phone = models.CharField(max_length=100)
   # address = models.CharField(max_length=100)

    #def __str__(self):
     #   return self.name

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_of_product')
    owners = models.ManyToManyField(User)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name