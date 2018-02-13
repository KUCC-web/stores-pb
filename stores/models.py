from django.db import models


class Store(models.Model):
    def __str__(self):
        return self.store_name
    store_name = models.CharField(max_length=20)
    store_stars = models.IntegerField(default=0)


class Product(models.Model):
    def __str__(self):
        return self.product_name
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_detail = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    product_stars = models.IntegerField(default=0)
    product_pub_date = models.DateTimeField('date published')
    viewer = models.IntegerField(default=0)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Review_pub_date = models.DateTimeField('date published')
    Review_text = models.CharField(max_length=200)
