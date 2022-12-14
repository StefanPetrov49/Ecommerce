from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    email = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    price = models.FloatField()

    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date_ordered = models.DateField(auto_now_add=True)

    complete = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    transaction_id = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    date_added = models.DateTimeField(
        auto_now_add=True
    )

class ShippingAddress(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    city = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.address
