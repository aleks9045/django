from django.shortcuts import render
from main.models import Information


def main_page(request):
    return render(request, 'main/index.html')


def about_us(request):
    information = Information.objects.all()
    return render(request, 'main/about.html', {'title': 'О нас', 'info': information})
