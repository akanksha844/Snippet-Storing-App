

from snippets.models import Snippet
from rest_framework import mixins
import genericpath
from  rest_framework import generics
from snippets.serializers import SnippetSerializer

class SnippetList(mixins.listModelMixin, mixins.CreateModelMixin, generics.GenericsAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
    
    def put(self, request, *args,**kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args,**kwargs)
      