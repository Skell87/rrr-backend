from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()

class Food(models.Model):
    title = models.TextField()
    category = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

# class CustomerOrderEndOfAllTable(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )

class Order(models.Model):
    customer =  models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    ticket_number = models.PositiveIntegerField()
    # can i have ticket number automatically increment from zero?
    # def __str__(self):
    #     return self.customer
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    food_item = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveBigIntegerField(default=0)
    