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
    email = models.EmailField(
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
    price = models.DecimalField(max_digits=7, decimal_places=2)

    image = models.ImageField(
        null=True,
        blank=True,
    )

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

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

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return str(self.id)


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

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


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
