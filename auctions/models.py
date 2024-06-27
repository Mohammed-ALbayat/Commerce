from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    created_at = models.DateField(default=date.today)

class Auctions(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    createdDate = models.DateField(default=date.today)
    description = models.TextField(max_length=100)
    img = models.ImageField(width_field=400, height_field=300)
    auctionOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctions")

class Comments:
    content = models.TextField(max_length=100)
    publishedDate = models.DateField(default=date.today)
    ownerComment = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionID = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="comments")

class Bids:
  value = models.IntegerField()
  ownerBid = models.ForeignKey(User, on_delete=models.CASCADE)
  auctionID = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="bids")
