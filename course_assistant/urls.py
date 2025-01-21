from django.urls import path

from .views import ask_question

urlpatterns = [
    path('ask-question/', ask_question, name='ask_question')
]