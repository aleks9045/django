from django.shortcuts import render, redirect
from main.models import Information
from main.forms import InformationForm


def main_page(request):
    return render(request, 'main/index.html')


def about_us(request):
    information = Information.objects.order_by('-id')
    return render(request, 'main/about.html', {'title': 'О нас', 'info': information})


def create_member(request):
    err = ''
    if request.method == 'POST':
        formm = InformationForm(request.POST)
        if formm.is_valid():
            formm.save()
            return redirect('home')
        else:
            err = 'Повторите заполнение формы'

    form = InformationForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
