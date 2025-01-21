from django.urls import path

from .views import relevant_papers

urlpatterns = [
    path('relevant-papers/', relevant_papers, name='relevant_papers')
]