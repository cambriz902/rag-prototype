from django.urls import path

from .views import recommend_papers

urlpatterns = [
    path('recommend-papers/', recommend_papers, name='recommend_papers')
]