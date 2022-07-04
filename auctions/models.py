from django.contrib.auth.models import AbstractUser
from django.db import models

# Keep in mind a class acts as our representation of each table
# When referring to class data we use the term attributes; it's methods for functions

class User(AbstractUser):
    pass

# Required to create a class to represent auction listings
# Each listing we create using this class is referred to as an instance
class Listing(models.Model):
    product = models.CharField(max_length = 255)
    price = models.DecimalField(decimal_places = 2, max_digits= 10)
    datePosted = models.DateTimeField()
    creator = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    # Will need  field which details whether or not a listing is active

# Class to represent bids
class Bids(models.Model):
    bidder = models.CharField(max_length= 255)
    bidPrice = models.DecimalField(decimal_places=2, max_digits=10)
    dateBid = models.DateTimeField()

# Comments on auction listings
class Comments(models.Model):
    commenter = models.CharField(max_length=255)
    comment = models.TextField()
    product = models.CharField(max_length=255)
    
