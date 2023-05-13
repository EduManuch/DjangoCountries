from django.shortcuts import render
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    context = {'name': "HELLO WORLD !"}
    return render(request, 'index.html', context)


def countries_list(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Language.objects.all()
    context = {'languages': languages}
    return render(request, 'languages-list.html', context)


def country_page(request, country):
    try:
        item = Country.objects.get(name=country)
        languages = item.languages.all()
        context = {'country': item.name,
                   'languages': languages}
        return render(request, 'country-page.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Страна {country} не найдена")

