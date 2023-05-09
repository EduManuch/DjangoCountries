import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCountries.settings")
application = get_wsgi_application()
from MainApp.models import Country, Language

with open("countries.json", 'r') as f:
    countries = json.load(f)

for item in countries:
    country = Country.objects.get(name=item['country'])
    for lang in item['languages']:
        country.languages.add(Language.objects.get(name=lang))
