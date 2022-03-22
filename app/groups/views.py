from rest_framework import generics
from groups.models import CustomUser, Group
from groups.serializers import UserSerializer, GroupSerializer

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