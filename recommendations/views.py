from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render

@api_view(['POST'])
def recommend_papers(request):
    print('hello')
    return Response(
            status=status.HTTP_200_OK,
            data={'papers': {'name': 'paper'}}
        )