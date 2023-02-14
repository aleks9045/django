from django.urls import path
from main.views import *


urlpatterns = [
    path('', main_page),
    path('about_us', about_us)

]
