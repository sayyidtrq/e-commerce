from django.forms import ModelForm
from main.models import ItemEntry
from django import forms
from django.utils.html import strip_tags

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ['name', 'price', 'description', 'rarity', 'rating', 'kategories', 'image_url']
        labels = {
            'name': 'Name',
            'price': 'Price',
            'description': 'Description',
            'rarity': 'Rarity',
            'rating': 'Rating',
            'kategories': 'Kategories',
            'image_url': 'Image URL'
        }

        def clean_name(self):
            name = self.cleaned_data.get['name']
            return strip_tags(name)
        
        def clean_price(self):
            price = self.cleaned_data.get['price']
            return strip_tags(price)
        
        def clean_description(self):
            description = self.cleaned_data.get['description']
            return strip_tags(description)
        
        def clean_rarity(self):
            rarity = self.cleaned_data.get['rarity']
            return strip_tags(rarity)
        
        def clean_rating(self):
            rating = self.cleaned_data.get['rating']
            return strip_tags(rating)
        
        def clean_kategories(self):
            kategories = self.cleaned_data.get['kategories']
            return strip_tags(kategories)
        
        def clean_image_url(self):
            image_url = self.cleaned_data.get['image_url']
            return strip_tags(image_url)
        