from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500,default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw0EOhjaJvqv0I6_sRj0h9Sf&ust=1676898737183000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPiK9NbWof0CFQAAAAAdAAAAABAJ")
