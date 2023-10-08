from django.urls import path

from regex.views import display_matching_patterns

urlpatterns = [
    path('', display_matching_patterns)
]