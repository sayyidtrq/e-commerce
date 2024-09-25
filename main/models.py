from django.db import models
from django.contrib.auth.models import User
import uuid

class ItemEntry (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField()
    rating = models.IntegerField()
    kategories = models.CharField(max_length=255, default='Sneakers')  
    time = models.DateTimeField(auto_now_add=True) 
