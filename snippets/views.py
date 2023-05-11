from audioop import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.parsers import JSONParser
from Tutorial2.snippets import serializers
from snippets.serializers import SnippetSerializer
from Tutorial2.snippets.models import Snippet
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST' ])  #function based views

def snippet_list(request, format=None):
    """ List all cpde snippets ,or create a new snippet """
    
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer =  SnippetSerializer(snippets, many= True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
    
@api_view([ 'GET', 'PUT', 'DELETE'])  # function based views

def snippet_detail(request, pk, format=None):
    """ Retrive, update or delete a code snippet """
    try:
        snippet = Snippet.objects.get(pk = pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == 'GET':
        serializer= SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status = 204)
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list',request= request, format=format ),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
    
        