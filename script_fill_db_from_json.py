import json
from MainApp.models import Country, Language

with open("countries.json", 'r') as f:
    countries = json.load(f)

lang_set = set()
for item in countries:
    country = Country(name=item['country'])
    country.save()
    for lang in item['languages']:
        lang_set.add(lang)

lang_list = sorted(list(lang_set))
for ln in lang_list:
    language = Language(name=ln)
    language.save()

