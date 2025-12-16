from django.db import models 
 
# Create your models here. 
class Category(models.Model): 
    cid=models.AutoField(primary_key=True) 
    cname=models.CharField(max_length=50) 
 
    def __str__(self): 
        return self.cname 
    
class Product(models.Model): 
    pid=models.AutoField(primary_key=True) 
    pname=models.CharField(max_length=50) 
    pdis=models.TextField() 
    pprice=models.FloatField() 
    pimage=models.ImageField(upload_to='products/') 
    cat=models.ForeignKey(Category,on_delete=models.CASCADE) 
 
    def __str__(self): 
        return self.pname
    
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
         return f"{self.user.username} - {self.product.pname} ({self.quantity})"
    
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('upi', 'UPI'),
        ('card', 'Debit/Credit Card'),
        ('netbanking', 'Net Banking')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    discount = models.FloatField(default=0)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()  # price per item

    def __str__(self):
        return f"{self.product.pname} ({self.quantity})"
