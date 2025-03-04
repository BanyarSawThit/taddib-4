from distutils.sysconfig import customize_compiler

from django.db import models

# Create your models here.
# Each table in the restaurant
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"

# Salad, Dishes, Soup, Desserts, Drinks
class Category(models.Model):
    category_title = models.CharField(max_length=100)
    cate_image = models.ImageField(default='taddib-icon.jpeg', blank=True)

    def __str__(self):
        return self.category_title

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_image = models.ImageField(default='supernova.jpg', blank=True)
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    has_meat_options = models.BooleanField(default=True)
    has_spicy_options = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} , {self.category.category_title}"

class Customization(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='customizations')
    meat = models.CharField(max_length=50, choices=[('Beef', 'Beef'), ('Chicken', 'Chicken'), ('None', 'None')])
    spicy_level = models.CharField(max_length=50, choices=[('Mild', 'Mild'), ('Medium', 'Medium'), ('High', 'High')])
    extra_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.item.name} ( meat-{self.meat} , spicy-{self.spicy_level})'

class UserOrder(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f'Order {self.id} , Table {self.table.table_number} ({self.status})'

class OrderItem(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    customization= models.ForeignKey(Customization, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customization.item.name} x {self.quantity} - Order {self.user_order.id}"