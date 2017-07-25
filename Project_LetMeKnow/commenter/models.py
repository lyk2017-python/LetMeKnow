from django.db import models

# This object holds firm name and firm id
class Firm(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=200)
    firm = models.ForeignKey(Firm)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    message = models.TextField()
    photo = models.ImageField()
    rate = models.PositiveSmallIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    #user - will be added
    #is_published - models.BooleanField(default=False) - comments that approved by admin will be published