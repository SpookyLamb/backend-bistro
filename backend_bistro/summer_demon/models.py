from django.db import models
import json

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=1.66)
    category = models.CharField(max_length=20)
    description = models.TextField()
    picture = models.ImageField()

    def __str__(self) -> str:
        return f"MENU ITEM | ID: {self.id} | NAME: {self.name} - PRICE: {self.price} - DESCRIPTION: {self.description}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    soul_flavor = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"CUSTOMER | ID: {self.id} | NAME: {self.name} - BIRTHDAY: {self.birthday} - SOUL FLAVOR: {self.soul_flavor}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    foods_ordered = models.ManyToManyField(MenuItem)
    quantities = models.TextField() #list corresponding (1:1, in order) to ordered items, stored as JSON string
    completed = models.BooleanField(default=False)

    def set_quantities(self, new: list):
        self.quantities = json.dumps(new)
    
    def get_quantities(self) -> list:
        return json.loads(self.quantities)
    
    def __str__(self) -> str:
        return f"ORDER | ID: {self.id} | FROM: {self.customer} - COMPLETED?: {self.completed}"
