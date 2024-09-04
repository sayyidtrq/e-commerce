from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jordan 1 Retro High OG',
        'price': 'IDR 2.000.000',
        'description': 'The Air Jordan 1 Retro High OG is a shoe that needs no introduction. It is the shoe that started it all. It is the first ever Air Jordan sneaker released back in 1985, created by the one and only Michael Jordan. The shoe was designed by Peter Moore and it was the only Air Jordan to feature the iconic Nike Swoosh logo. The Air Jordan 1 is still popular today, and has been released in more colorways than any other Air Jordan model.',
        'rarity': '7',
        'rating': '9'
    }

    return render(request, "main.html", context)
