from django.db import models

from django.urls import reverse #allows us to create urls

# Create your models here.
#Categories for dresses, shoes, tops, pants.....

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)#no repeated category

    class Meta:

        verbose_name_plural = 'categories' # by default add 's' to the plural, override it with correct form.
    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])


    
class Product(models.Model):

    #FK  link the product with a category
    #on_delete --> if the category is deleted, so do products under this category
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)#longer

    slug = models.SlugField(max_length=255, unique=True)

    price = models.DecimalField(max_digits=4, decimal_places=2) #4 in total, and with 2 digits allowed after the decimal point

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products' # by default add 's' to the plural, override it with correct form.
    
    # Product(1) --> title
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])











