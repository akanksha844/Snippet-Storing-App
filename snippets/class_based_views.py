
from django.contrib.auth.models import User
from django.http import Http404
from requests import Response
from Tutorial2.snippets import serializers
from Tutorial2.snippets.models import Snippet
from Tutorial2.snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import status, generics
from rest_framework import permissions
from rest_framework import renderers


class SnippetList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """  List all snippet, or create a new snippet """
   
    
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self,request, format=None):
        serializer= SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    
    
    
class SnippetDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    """ Retrieve, update or delete a snippet instance """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self,request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet= self.get_object(pk)
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class UserList(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetriveAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
class SnippetHighlight(generics.GenericsAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]
    
    def get(self, request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighetd)
    
    
    
        
        