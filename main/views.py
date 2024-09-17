from django.shortcuts import render, redirect
from main.models import ItemEntry
from main.forms import ItemEntryForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    itemEntry = ItemEntry.objects.all()

    context = {
        'nama_orang': 'Sayyid Thariq',
        'npm': '2306275714',
        'kelas': 'Kelas B',
        'name': 'Jordan 1 Retro High OG',
        'price': 'IDR 2.000.000',
        'description': 'The Air Jordan 1 Retro High OG is a shoe that needs no introduction. It is the shoe that started it all. It is the first ever Air Jordan sneaker released back in 1985, created by the one and only Michael Jordan. The shoe was designed by Peter Moore and it was the only Air Jordan to feature the iconic Nike Swoosh logo. The Air Jordan 1 is still popular today, and has been released in more colorways than any other Air Jordan model.',
        'rarity': '7',
        'rating': '9',
        'kategories': 'Sneakers',
        'itemEntry': itemEntry,
    }

    return render(request, "main.html", context)

def show_item(request, item_id):
    item = ItemEntry.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, "item.html", context)

def create_item(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
