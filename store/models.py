from django.db import models
from category.models import Category
from django.urls import reverse  

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)  # Added comma after max_length=200
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()  # Corrected misspelling of IntegerField
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()  # Corrected misspelling of IntegerField
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Corrected on_delete argument
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
