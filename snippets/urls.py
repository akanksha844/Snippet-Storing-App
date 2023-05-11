

from os import path
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from django import views,class_based_views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from Tutorial2.snippets.viewset import SnippetViewSet, UserViewSet


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', class_based_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', class_based_views.SnippetDetail.as_view()),
    path('users/', class_based_views.UserList.as_view()),
    path('users/<int:pk>/', class_based_views.UserDetail.as_view()),
    path('snippets/<int:pk>/highlight/', class_based_views.SnippetHighlight.as_view()),
    
    
    
]

urlpatterns = format_suffix_patterns([
    path('', views.api_root), 
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', class_based_views.SnippetList.as_view(), name='sippet-list'),
    
])

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
    
})

snippet_detail= SnippetViewSet.as_view({
    'get' : 'retrieve',
    'put': 'update',
    'patch' : 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
},renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
    
    
router = DefaultRouter()
router.register(r'snippets',views.SnippetViewSet, basename="snippet" )
router.register(r'users', views.UserViweSet, basename="user")


urlpatterns= [
    path('', include(router.urls)),
]
                                           