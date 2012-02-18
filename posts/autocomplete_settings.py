from django.shortcuts import render_to_response
from autocomplete.views import AutocompleteSettings
from posts.models import *
from posts.views import autocomplete

class ProfessionAutocomplete(AutocompleteSettings):
    queryset = Profession.objects.all()
    search_fields = ('^name',)

autocomplete.register('posts.profession', ProfessionAutocomplete)

