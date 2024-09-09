from django.db import models

class ItemEntry (models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField(max_length=2)
    rating = models.IntegerField(max_length=2)
    kategories = models.CharField(max_length=255)

