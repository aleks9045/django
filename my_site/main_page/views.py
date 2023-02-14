from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page/index.html')


def about_us(request):
    return render(request, 'main_page/index2.html')
