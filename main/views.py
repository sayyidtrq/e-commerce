from django.shortcuts import render, redirect, reverse
from main.models import ItemEntry
from main.forms import ItemEntryForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    context = {
        'nama_orang': request.user.username,
        'name': '2009 Barcelona Jersey',
        'price': 'Rp. 1.000.000',
        'description': 'Jersey Barcelona tahun 2009 yang dipakai saat final UCL 2009',
        'rarity': 'Legendary',
        'rating': '10',
        'kategories': 'Jersey',
        'nama_owner': 'Sayyid',
        'npm': '2306275714',
        'kelas': 'Kelas B',
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_item(request, item_id):
    item = ItemEntry.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, "item.html", context)

def create_item(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        itemEntry = form.save(commit=False)
        itemEntry.user = request.user
        itemEntry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_item.html", context)

@csrf_exempt
@require_POST
def create_item_ajax(request):
    user = request.user
    name = strip_tags(request.POST.get('name'))
    price = strip_tags(request.POST.get('price'))
    description = strip_tags(request.POST.get('description'))
    rarity = strip_tags(request.POST.get('rarity'))
    rating = strip_tags(request.POST.get('rating'))
    kategories = strip_tags(request.POST.get('kategories'))
    image_url = strip_tags(request.POST.get('image_url'))

    new_item = ItemEntry(
        user=user,
        name=name,
        price=price,
        description=description,
        rarity=rarity,
        rating=rating,
        kategories=kategories,
        image_url=image_url
    )

    new_item.save()

    return HttpResponse(b"CREATED ITEM", status=201)
                                                                                                                                            

def edit_item(request, id):
    item = ItemEntry.objects.get(pk=id)

    form = ItemEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get mood berdasarkan id
    item = ItemEntry.objects.get(pk=id)
    # Hapus mood
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = ItemEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
            messages.error(request, 'Invalid username or password.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


