from django.urls import path
from main_page.views import *


urlpatterns = [
    path('', main_page),
    path('about_us', about_us)

]
