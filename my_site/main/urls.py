from django.urls import path
from main.views import *


urlpatterns = [
    path('', main_page, name='home'),
    path('about_us', about_us, name='about'),
    path('create_member', create_member, name='create')

]
