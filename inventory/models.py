from django.db import models
from django.core.validators import MinValueValidator
class Product(models.Model):
    sku = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=150)
    opening_stock = models.PositiveIntegerField(default=0)
    def __str__(self): return self.name
class Transaction(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    kind = models.CharField(max_length=8,choices=[('purchase','Purchase'),('sale','Sale')])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=12,decimal_places=2,validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
