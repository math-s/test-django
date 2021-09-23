from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"

class Sale(models.Model):
    client = models.CharField(max_length=255)
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.client} {self.date}"


class Item(models.Model):
    sale = models.ForeignKey("checkout.Sale", on_delete=models.CASCADE)
    product = models.ForeignKey("checkout.Product", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sale.client} {self.product.name} {self.price}"