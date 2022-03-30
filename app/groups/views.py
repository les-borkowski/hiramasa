from rest_framework import generics
from groups.models import CustomUser, Group, Event
from groups.serializers import UserSerializer, GroupSerializer, EventSerializer

# users view
class UserList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAdminUser]
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAdminUser]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# groups views    
class GroupList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAdminUser]
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAdminUser]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventList(generics.ListCreateAPIView):
    # permission_classes = [permissions.isAuthenticated]
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer    

class EventDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.isAuthenticated]
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer    