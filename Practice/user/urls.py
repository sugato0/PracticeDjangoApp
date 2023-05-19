




from django.contrib import admin
from django.urls import path,include

from .views import RegistrUserView,SomeDataView



urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registr'),
    path('someData/', SomeDataView.as_view(), name='someData'),
    # path('login/')


]
