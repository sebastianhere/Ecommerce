from django.db import models
import django.utils.dateformat


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_img", blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Products(models.Model):
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    pname = models.CharField(max_length=300, blank=True, null=False)
    org_price = models.FloatField(blank=True, null=False)
    sell_price = models.FloatField(blank=True, null=False)
    quantity = models.IntegerField()
    img = models.ImageField(upload_to="pictures", blank=False, null=False)
    pro_desc = models.TextField()
    stocks = models.IntegerField(default=10)


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=False, null=False)
    cart_date = models.DateTimeField(auto_now_add=True)


class Items(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def Total(self):
        return self.products.sell_price * self.quantity

    # def Ftotal(self):
    #
    #     return  (self.products.discount_p*self.quantity)+45


def __str__(self):
    return self.pname


from django.db import models

# Create your models here.
