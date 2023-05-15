# from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list/', views.countries_list, name='countries-list'),
    path('languages-list/', views.languages_list, name='languages-list'),
    path('country/<str:country>', views.country_page, name='country-detail'),
]
