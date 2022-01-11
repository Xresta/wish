from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import SlugField
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_creator')
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_updator')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, default="momo")
    image = models.ImageField(upload_to='images/', default =True)
    #desciption = models. TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_updator')
    

    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name