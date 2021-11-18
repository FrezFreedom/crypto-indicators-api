from django.urls import path

from .views import atr

urlpatterns = [
    path('atr/', atr),
]
