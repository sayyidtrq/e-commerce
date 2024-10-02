from django.forms import ModelForm
from main.models import ItemEntry

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