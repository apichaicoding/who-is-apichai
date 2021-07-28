from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home-page"),
    path('Services/', Services, name="services"),
     path('Contact/', Contact, name="contact"),
]
