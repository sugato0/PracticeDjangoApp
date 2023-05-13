




from django.contrib import admin
from django.urls import path,include

from .views import RegistrUserView



urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registr'),

]
