from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuario")
    is_active = models.BooleanField(default=True, verbose_name="activo")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="fecha de orden")

    def __str__(self):
        return f"order {self.id} by {self.user}"

class OrderProduct(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="orden")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="producto") 
    quantity = models.IntegerField(verbose_name="cantidad")

    def __str__(self):
        return f"{self.order} - {self.product}"