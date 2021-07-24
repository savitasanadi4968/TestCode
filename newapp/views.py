from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from newapp.models import newapps
from newapp.serializers import newappSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def newapp_list(request):


# GET list of tutorials, POST a new tutorial, DELETE all tutorials


@api_view(['GET', 'PUT', 'DELETE'])
def newapp_detail(request, pk):
    # find tutorial by pk (id)
    try:
        newapps = newapp.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial


@api_view(['GET'])
def newapp_list_published(request):
# GET all published tutorials