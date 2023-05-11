from requests import Response
from rest_framework import viewsets
from Tutorial2.snippets import permissions
from Tutorial2.snippets.models import Snippet
from rest_framework.decorators import action

from Tutorial2.snippets.serializers import SnippetSerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ This viewset automatically provides 'list' and 'retrive' actions """
    
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    
class SnippetViewSet(viewsets.ModelViewSet):
    """ This viewset automatically provides 'list', 'create', 'retrive','update', 'destroy' actions
    
    Addtionally extra 'highlist' actions """
    
    queryset = Snippet.objectsa.all()
    serializer_class = SnippetSerializer
    permission_classes =n[permissions.IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    