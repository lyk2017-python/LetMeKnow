from django.db import models


class Firm(models.Model):
    """Class for firm"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "#{id} {name}".format(id=self.id, name=self.name)


class Product(models.Model):
    """Class for product"""
    name = models.CharField(max_length=200)
    firm = models.ForeignKey(Firm)

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    """Class for comment"""
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    message = models.TextField()
    photo = models.ImageField()
    rate = models.PositiveSmallIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    #user - will be added
    #is_published - models.BooleanField(default=False) - comments that approved by admin will be published