from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    Username = None
    Contact = models.CharField(blank=True,max_length=12)
    email = models.CharField(unique=True, max_length=50, primary_key=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    class Meta:
        db_table = "Users"


# Create your models here.
class Product(models.Model):
    Product_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=255)
    Product_category = models.CharField(max_length=255)
    Product_image = models.ImageField(upload_to='product_img')
    Product_price = models.DecimalField( max_digits=10, decimal_places=2)
    Product_quantity = models.IntegerField()
    Product_description = models.CharField(max_length=500)

    class Meta:
        db_table = 'Product'

class Cart(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def Total_price(self):
        return self.quantity * self.Product.Product_price

    class Meta:
        db_table = 'Cart'

class Wishlist(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Wishlist'