from django.urls import path
from diffusione.views import homepage

urlpatterns = [
    path('', homepage, name='home')
]