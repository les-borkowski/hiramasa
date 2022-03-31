from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from groups import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
    path('groups/', views.GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)